import os

import requests
from config import DATA_FILENAME, STANFORD_QA_DATA_LINK


def download_file(url):
    try:
        response = requests.get(url)
        if response.ok:
            if not os.path.exists(DATA_FILENAME):
                with open(DATA_FILENAME, "wb") as file:
                    file.write(response.content)
                print(f"File '{DATA_FILENAME}' has been downloaded successfully!")
            else:
                print(f"File '{DATA_FILENAME}' already exists. Skipping download.")
        else:
            print("Failed to download the file. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error downloading the file:", e)


if __name__ == "__main__":
    download_file(STANFORD_QA_DATA_LINK)
