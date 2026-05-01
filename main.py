from aiogram.types import BotCommand
from aiogram import Dispatcher
from init import bot
from hand import router
import asyncio


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