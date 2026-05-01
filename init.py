from aiogram import Bot
import os
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token = token)