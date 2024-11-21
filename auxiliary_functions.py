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


def take_files(directory):
    filesindir = os.listdir(directory)
    image_paths = []

    for filesindirs in filesindir:
        path = os.path.join(directory, filesindirs)
        image_paths.append(path)
        shuffle(image_paths)
    return image_paths


def download_and_save_image(img_url, path, img_number, apy_key=None):
    params = {
        'api_key': apy_key
    }
    img_response = requests.get(img_url, params=params)
    img_response.raise_for_status()

    extension = get_extension_file(img_url)
    with open(f'{path}/image_{img_number}{extension}', 'wb') as file:
        file.write(img_response.content)
