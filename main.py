from urllib.parse import urlparse
from datetime import datetime
from dotenv import load_dotenv
import requests
import pathlib
import os


def download_img(url, path):
    filename = 'hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()
    with open(path/filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(spacex_id, path):
    url = f'https://api.spacexdata.com/v5/launches/{spacex_id}'
    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()

    list_img_spacex = answer['links']['flickr']['original']

    for img_number, img_url in enumerate(list_img_spacex):
        img_response = requests.get(img_url)
        img_response.raise_for_status()

        with open(f'{path}/spacex_{img_number}.jpeg', 'wb') as file:
            file.write(img_response.content)


def get_extension_file(url):
    parse = urlparse(url)
    path = parse[2]
    return os.path.splitext(path)[1]


def saving_img_nasa(nasa_api_key, path):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_api_key,
        'count': 30
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    answer = response.json()

    img_urls = []
    for item in answer:
        if 'url' in item:
            img_urls.append(item['url'])

    for img_number, img_url in enumerate(img_urls):
        img_response = requests.get(img_url)
        img_response.raise_for_status()

        with open(f'{path}/nasa_apod_{img_number}.jpeg', 'wb') as file:
            file.write(img_response.content)


def saving_img_epic(nasa_api_key, path, count_images):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_api_key
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    answer = response.json()

    for index, record in enumerate(answer[:count_images]):
        img_key = record['image']
        img_data = record['date']

        img_data = datetime.strptime(img_data, "%Y-%m-%d %H:%M:%S")
        year = img_data.year
        month = img_data.month
        day = img_data.day

        img_url = f'https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{img_key}.png'
        img_response = requests.get(img_url, params=params)
        img_response.raise_for_status()

        with open(f'{path}/nasa_epic_{index+1}.png', 'wb') as file:
            file.write(img_response.content)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']
    spacex_id = os.environ['SPACEX_ID']

    path = pathlib.Path('image')
    path.mkdir(parents=True, exist_ok=True)

    saving_img_epic(nasa_api_key, path, 5)
