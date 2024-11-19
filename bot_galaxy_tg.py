import telegram
from dotenv import load_dotenv
import os


load_dotenv()
telegram_access_token = os.environ['TELEGRAM_ACCESS_TOKEN']

bot = telegram.Bot(token=telegram_access_token)

bot.send_message(chat_id='@galaxy_nasa_bot', text="Извини, я тут пытаюсь с ботом в телеграм разобраться. (Пишет Бот)")
