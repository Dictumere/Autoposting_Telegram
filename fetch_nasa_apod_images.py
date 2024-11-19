import requests
import os
import pathlib
from dotenv import load_dotenv
from auxiliary_functions import get_extension_file


def saving_nasa_apod(nasa_api_key, path):
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

        extension = get_extension_file(img_url)
        with open(f'{path}/nasa_apod_{img_number}.{extension}', 'wb') as file:
            file.write(img_response.content)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_key = os.environ['NASA_API_KEY']

    path = pathlib.Path('image_nasa_apod')
    path.mkdir(parents=True, exist_ok=True)

    saving_nasa_apod(nasa_api_key, path)
