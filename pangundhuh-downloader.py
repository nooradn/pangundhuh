import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# 🔧 Config
DOWNLOAD_DIR = './downloads'
SOURCE_FILE = 'list.txt'
MAX_WORKERS = 50  # ✅ Untuk file kecil, aman dinaikkan

# 📁 Make sure download dir exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# 🔥 Persistent session with retry
def create_session():
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=0.2,
        status_forcelist=[500, 502, 503, 504],
        allowed_methods=["GET"]
    )
    adapter = HTTPAdapter(
        max_retries=retries,
        pool_connections=MAX_WORKERS,
        pool_maxsize=MAX_WORKERS
    )
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

session = create_session()

# 🚀 Download function
def download_file(url):
    try:
        filename = os.path.basename(url)
        local_path = os.path.join(DOWNLOAD_DIR, filename)

        with session.get(url, timeout=30) as r:
            r.raise_for_status()
            with open(local_path, 'wb') as f:
                f.write(r.content)

        return (url, True, None)
    except Exception as e:
        return (url, False, str(e))

# 🔗 Load URLs
with open(SOURCE_FILE) as f:
    urls = [line.strip() for line in f if line.strip()]

# 🚀 Start downloading with ThreadPool
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    futures = {executor.submit(download_file, url): url for url in urls}

    for future in tqdm(as_completed(futures), total=len(futures), desc="Downloading"):
        url = futures[future]
        try:
            url, success, error = future.result()
            if not success:
                print(f"❌ Failed {url}: {error}")
        except Exception as e:
            print(f"❌ Error {url}: {e}")

print("🎉 Done!")
