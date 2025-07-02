# Pangundhuh - Downloader Tool

🚀 A lightweight, multithreaded file downloader in Python — optimized for speed and simplicity. Supports retry logic, concurrent downloads, and progress tracking via `tqdm`.

---

## 🇮🇩 Why "Pangundhuh"?

> **Pangundhuh** is a word from the Javanese language that means **"the one who downloads"** or **"the harvester"**.  
> Derived from the root word **"undhuh"** (to download, to collect, or to harvest),  
> it reflects the purpose of this tool: **to fetch and collect resources efficiently.**

This name honors local language identity while remaining functional and relevant to a global audience.

---

## ✨ Features

- 🧵 Multithreaded for faster downloads (`ThreadPoolExecutor`)
- ♻️ Retry logic (customizable attempts)
- 📦 Save files automatically to the local directory
- 📊 Beautiful progress bar with `tqdm`
- 🧼 Clean and minimal code

---

## 📂 Folder Structure

```
.
├── pangundhuh-downloader.py
├── list.txt                  # List of URLs to download (one per line)
├── downloads/                # Output folder for downloaded files, will be created if not exist
```

---

## ⚙️ Configuration

Edit the values at the top of `pangundhuh-downloader.py`:

```python
DOWNLOAD_DIR = './downloads'    # Folder to save files
SOURCE_FILE = 'list.txt'        # File containing list of URLs
MAX_WORKERS = 50                # Number of concurrent threads
RETRY_TIMES = 3                 # Retry count for failed downloads
TIMEOUT = 30                    # Request timeout in seconds
```

---

## 📄 Usage

1. **Install required packages:**
   ```bash
   pip install requests tqdm
   ```

2. **Add your download URLs** to `list.txt`, one per line.

3. **Run the script:**
   ```bash
   python pangundhuh-downloader.py
   ```
   Or simply double-click the `pangundhuh-downloader.py` file directly from Windows Explorer.

---

## 🧪 Example

Contents of `list.txt`:
```
https://example.com/image1.jpg
https://example.com/image2.jpg
```

When run, all files will be saved to `./downloads/` with filenames extracted from the URL.

---

## ✅ Requirements

- Python 3.6+
- `requests`
- `tqdm`

---

## 📄 License

MIT — feel free to use and modify.
