from dotenv import load_dotenv
from aiogram import Bot
import os


load_dotenv()
token = os.getenv('TG_BOT_TOKEN')
bot = Bot(token = token)