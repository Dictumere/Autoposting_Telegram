import telegram
import os
import time
import argparse
from dotenv import load_dotenv
from auxiliary_functions import takeFiles


def publish_img(telegram_access_token, tg_chat_id, path, hours=14800):
    bot = telegram.Bot(token=telegram_access_token)
    ls_image_nasa_epic = takeFiles(path)
    for img in ls_image_nasa_epic:
        bot.send_photo(chat_id=tg_chat_id, photo=open(img, 'rb'))
        time.sleep(int(hours) * 3600)


if __name__ == '__main__':
    load_dotenv()
    telegram_access_token = os.environ['TELEGRAM_ACCESS_TOKEN']
    hours = os.environ['HOURS']
    tg_chat_id = os.environ['TG_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('path_dir_images',
                        type=str,
                        nargs='?',
                        default='images_nasa_epic')
    path_dir_images = parser.parse_args().path_dir_images

    publish_img(telegram_access_token, tg_chat_id, path_dir_images, hours)
