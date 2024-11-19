import telegram
from dotenv import load_dotenv
import os


load_dotenv()
telegram_access_token = os.environ['TELEGRAM_ACCESS_TOKEN']

bot = telegram.Bot(token=telegram_access_token)

bot.send_photo(chat_id='@galaxy_nasa_bot',
                  photo=open('image_nasa_epic/nasa_epic_1.png', 'rb'))
