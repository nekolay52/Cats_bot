from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from hand import router
import asyncio
import os


load_dotenv()
token = os.getenv('TOKEN')
bot = Bot(token = token)
dispatcher = Dispatcher()


async def main_menu(bot):
    command = [
        BotCommand(command = "start", description = "Просто попробуй нажать :)"),
    ]
    await bot.set_my_commands(command)


async def main_function():
    await main_menu(bot)
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)


asyncio.run(main_function())

