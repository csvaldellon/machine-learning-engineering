import os

import requests
from config import STANFORD_QA_DATA_LINK


def download_file(url):
    try:
        response = requests.get(url)
        if response.ok:
            filename = url.split("/")[-1]
            if not os.path.exists(filename):
                with open(filename, "wb") as file:
                    file.write(response.content)
                print(f"File '{filename}' has been downloaded successfully!")
            else:
                print(f"File '{filename}' already exists. Skipping download.")
        else:
            print("Failed to download the file. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error downloading the file:", e)


if __name__ == "__main__":
    download_file(STANFORD_QA_DATA_LINK)
