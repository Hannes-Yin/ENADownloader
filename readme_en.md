# ENA FTP File Downloader

This is a Python script for downloading FASTQ files from the European Nucleotide Archive (ENA). The script retrieves data for a specified accession by accessing the ENA API and uses multithreading to download the related FASTQ files concurrently.

## Features

- **Multithreaded Downloading**: Utilizes `ThreadPoolExecutor` to enable concurrent downloads, improving speed.
- **Error Handling**: Keeps track of failed downloads and prompts the user to retry if necessary.
- **Folder Management**: Automatically creates a folder named after the accession and saves all downloaded files in it.
- **File Existence Check**: Checks if the file already exists in the target folder before downloading to prevent duplicates.

## Installation

Ensure you have installed the required Python libraries. You can install them using the following command:

```bash
pip install requests tqdm
```

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ena-ftp-downloader.git
cd ena-ftp-downloader
```

### 2. Run the Script

```bash
python downloader.py
```

### 3. Enter Accession

After running the script, you will be prompted to enter an ENA accession number. Once entered, the script will start downloading the related files.

```plaintext
Enter accession value: ERP008930
```

### 4. Download Progress

The script displays a progress bar and prints a success message once each file is downloaded.

### 5. Error Handling

If some files fail to download, the script will prompt you to retry.

```plaintext
X files failed to download. Retry? (y/n):
```

## Example

If you want to download files related to the accession `ERP008930`, run the script and enter `ERP008930`. The script will create a folder named `ERP008930` and save all downloaded FASTQ files inside it.

## Notes

- Ensure you have sufficient disk space to store the downloaded files.
- If you need to download large datasets, it's recommended to run the script in a stable network environment.
- Since anonymous FTP login is used, some sensitive data may not be available for download.

## Contributions

Contributions of any kind are welcome, including code improvements, bug fixes, and documentation enhancements. Please submit a Pull Request or open an Issue.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.

