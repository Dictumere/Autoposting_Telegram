import requests
import pathlib
import argparse
from auxiliary_functions import download_and_save_image


def fetch_spacex_images(spacex_id_launch, path):
    url = f'https://api.spacexdata.com/v5/launches/{spacex_id_launch}'

    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()

    img_spacex = answer['links']['flickr']['original']

    for img_number, img_url in enumerate(img_spacex):
        download_and_save_image(img_url, path, img_number)


if __name__ == '__main__':
    path = pathlib.Path('images_spacex')
    path.mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(description='Получает фотографии с запусков ракет SpaceX')
    parser.add_argument('spacex_id_launch',
                        type=str,
                        nargs='?',
                        default='latest',
                        help='ID запуска ракеты')
    spacex_id_launch = parser.parse_args().spacex_id_launch

    fetch_spacex_images(spacex_id_launch, path)
