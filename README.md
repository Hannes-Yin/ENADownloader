# ENA FTP File Downloader

这是一个用于从欧洲核苷酸档案馆（ENA）下载 FASTQ 文件的 Python 脚本。该脚本通过访问 ENA API 获取指定 accession 的数据，并使用多线程并发下载相关的 FASTQ 文件。

## 特点

- **多线程下载**：利用 `ThreadPoolExecutor` 实现并发下载，提高下载速度。
- **错误处理**：记录下载失败的文件，并在最后询问用户是否需要重试。
- **文件夹管理**：自动创建以 accession 命名的文件夹，并将所有下载的文件保存到该文件夹中。
- **文件存在检查**：在下载前检查文件是否已经存在于目标文件夹中，避免重复下载。

## 安装依赖

确保你已经安装了所需的 Python 库。你可以使用以下命令安装这些库：

```bash
pip install requests tqdm
```

## 使用方法

### 1. 克隆仓库

```bash
git clone https://github.com/yourusername/ena-ftp-downloader.git
cd ena-ftp-downloader
```

### 2. 运行脚本

```bash
python downloader.py
```

### 3. 输入 Accession

运行脚本后，程序会提示你输入一个 ENA accession 值。输入完成后，脚本将开始下载相关文件。

```plaintext
请输入 accession 值：ERP008930
```

### 4. 下载进度

脚本会显示下载进度条，并在每个文件下载完成后打印成功消息。

### 5. 错误处理

如果某些文件下载失败，脚本会在最后询问你是否需要重试。

```plaintext
有 X 个文件下载失败，是否重试？(y/n):
```

## 示例

假设你想下载 accession 为 ERP008930 的相关文件，运行脚本后输入 ERP008930，脚本将会创建一个名为 `ERP008930` 的文件夹，并将所有下载的 FASTQ 文件保存到该文件夹中。

## 注意事项

- 确保你有足够的磁盘空间来存储下载的文件。
- 如果你需要下载大量数据，建议在网络状况良好的环境下运行脚本。
- 由于使用的是匿名 FTP 登录，某些敏感数据可能无法下载。

## 贡献

欢迎任何形式的贡献，包括但不限于代码改进、Bug 修复和文档优化。请提交 Pull Request 或 Issues。

## 许可证

本项目采用 MIT 许可证。详细信息请参阅 `LICENSE` 文件。
