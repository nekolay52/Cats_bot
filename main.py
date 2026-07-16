from list_slide_handlers import list_slide_router
from lists_handlers import list_router
from aiogram.types import BotCommand
from aiogram import Dispatcher
from handlers import router
from init import bot
import asyncio


dispatcher = Dispatcher()


async def main_menu(bot):
    command = [
        BotCommand(command = "start", description = "Старт бота"),
    ]
    await bot.set_my_commands(command)


async def main_function():
    await main_menu(bot)
    dispatcher.include_router(router)
    dispatcher.include_router(list_router)
    dispatcher.include_router(list_slide_router)
    await dispatcher.start_polling(bot)


asyncio.run(main_function())