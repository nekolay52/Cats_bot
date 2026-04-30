from aiogram import F, Router
from aiogram.filters import Command
from butt import button_start, button_spisok
from aiogram.types import Message
from tools import get_directory_tree
from get_cat import get_cat
import os


router = Router()


@router.message(Command('start'))
async def hello_world(message):
    if str(message.from_user.id) not in os.listdir("users_pictures"):
        os.makedirs(f"users_pictures/{message.from_user.id}")
    await message.answer("О привет! Выбери пожалуйста что ты хочешь делать :)", reply_markup=button_start)
    print("Кнопка <start> нажата")


@router.message(Command('info'))
async def hello_world(message):
    l = get_directory_tree("./")
    await message.answer(f"```\n{l}\n```", reply_markup=button_start, parse_mode="Markdown")
    print("Кнопка <info> нажата")


@router.message(F.text == 'Списки котиков')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Списки котиков> нажата")

@router.message(F.text == 'Добавить список')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Добавить список> нажата")

@router.message(F.text == 'Удалить список')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Удалить список> нажата")

@router.message(F.text == 'Просмотреть список')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Просмотреть список> нажата")


@router.message(F.text == 'Получить котика')
async def hello_world(message):
    get_cat("temp")
    await message.answer(":)")
    print("Кнопка <Получить котика> нажата")


@router.message(F.text == 'Назад')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_start)
    print("Кнопка <Назад> нажата")

