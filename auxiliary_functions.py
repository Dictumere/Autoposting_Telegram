import os
from urllib.parse import urlparse
import requests


def get_extension_file(url):
    parse = urlparse(url)
    path = parse[2]
    return os.path.splitext(path)[1]


def download_img(url, path):
    filename = 'hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()
    with open(path/filename, 'wb') as file:
        file.write(response.content)
