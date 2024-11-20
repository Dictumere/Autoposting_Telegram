import os
from urllib.parse import urlparse
import requests
from random import shuffle


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


try:
    def take_files(directory):
        filesindir = os.listdir(directory)
        image_paths = []

        for filesindirs in filesindir:
            path = os.path.join(directory, filesindirs)
            image_paths.append(path)
            shuffle(image_paths)
        return image_paths
except FileNotFoundError:
    print('Файл не обнаружен')
