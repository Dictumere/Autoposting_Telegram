from datetime import datetime
from dotenv import load_dotenv
import requests
import pathlib
import os


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