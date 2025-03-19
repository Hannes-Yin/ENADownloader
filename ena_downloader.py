import ftplib
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import requests

def fetch_data(accession):
    url = f"https://www.ebi.ac.uk/ena/portal/api/filereport?accession={accession}&result=read_run&fields=study_accession,sample_accession,experiment_accession,run_accession,tax_id,scientific_name,fastq_ftp,submitted_ftp,sra_ftp,bam_ftp&format=json&download=true&limit=0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []

def download_file_ftp(ftp_url, folder_path):
    try:
        # 解析URL
        parsed_url = ftp_url.replace('ftp://', '').split('/')
        server = parsed_url[0]
        file_path = '/'.join(parsed_url[1:-1])
        filename = parsed_url[-1]

        local_filepath = os.path.join(folder_path, filename)

        # 检查文件是否已经存在
        if os.path.exists(local_filepath):
            print(f'\n文件 {filename} 已经存在，跳过下载')
            return filename

        # 连接到FTP服务器并下载文件
        with ftplib.FTP(server) as ftp:
            ftp.login(user='anonymous')  # 默认匿名登录
            if file_path:
                ftp.cwd(file_path)
            with open(local_filepath, 'wb') as local_file:
                def callback(data):
                    local_file.write(data)
                ftp.retrbinary(f'RETR {filename}', callback)
        print(f'\n成功下载文件 {filename}')
        return filename
    except ftplib.all_errors as e:
        print(f'\n{ftp_url} 下载失败: {e}')
        return None

def main():
    accession = input("请输入accession值：")
    items = fetch_data(accession)

    urls = [item['fastq_ftp'] for item in items if 'fastq_ftp' in item]

    # 创建以accession命名的文件夹
    folder_path = accession
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    failed_downloads = []
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(download_file_ftp, url, folder_path): url for url in urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc='下载进度'):
            url = futures[future]
            try:
                result = future.result()
                if result is None:
                    failed_downloads.append(url)
            except Exception as exc:
                print(f'\n{url} 处理异常: {exc}')
                failed_downloads.append(url)

    if failed_downloads:
        retry = input(f"\n有 {len(failed_downloads)} 个文件下载失败，是否重试？(y/n): ")
        if retry.lower() == 'y':
            for url in failed_downloads:
                download_file_ftp(url, folder_path)

if __name__ == "__main__":
    main()



