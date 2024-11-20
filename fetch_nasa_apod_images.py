import requests
import os
import pathlib
import argparse
from dotenv import load_dotenv
from auxiliary_functions import download_and_save_image


def save_nasa_apod_images(nasa_api_key, path, count_images):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': nasa_api_key,
        'count': count_images
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    answer = response.json()

    img_urls = []
    for image_data in answer:
        if 'url' in image_data:
            img_urls.append(image_data['url'])

    for img_number, img_url in enumerate(img_urls):
        download_and_save_image(img_url, path, img_number)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    path = pathlib.Path('images_nasa_apod')
    path.mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(description='Получает изображения или фотоснимки из Вселенной.')
    parser.add_argument('count_images',
                        type=int,
                        nargs='?',
                        default='30',
                        help='Количество фотографий для загрузки')
    count_images = parser.parse_args().count_images

    save_nasa_apod_images(nasa_api_key, path, count_images)
