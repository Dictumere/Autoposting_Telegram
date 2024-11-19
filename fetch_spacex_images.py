import requests
import pathlib
import argparse
from auxiliary_functions import get_extension_file


def fetch_spacex_images(spacex_id_launch, path):
    url = f'https://api.spacexdata.com/v5/launches/{spacex_id_launch}'

    response = requests.get(url)
    response.raise_for_status()
    answer = response.json()

    list_img_spacex = answer['links']['flickr']['original']

    for img_number, img_url in enumerate(list_img_spacex):
        img_response = requests.get(img_url)
        img_response.raise_for_status()

        extension = get_extension_file(img_url)
        with open(f'{path}/spacex_{img_number}.{extension}', 'wb') as file:
            file.write(img_response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('spacex_id_launch',
                        type=str,
                        nargs='?',
                        default='latest')
    spacex_id_launch = parser.parse_args().spacex_id_launch

    path = pathlib.Path('images_spacex')
    path.mkdir(parents=True, exist_ok=True)

    fetch_spacex_images(spacex_id_launch, path)
