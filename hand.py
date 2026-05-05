from aiogram import F, Router
from aiogram.filters import Command
from butt import button_start, button_spisok, button_inline
from aiogram.types import Message, CallbackQuery
from tools import get_directory_tree
from get_cat import get_cat
from aiogram import types
from init import bot
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
async def hello_world(message, state):
    get_cat(f"users_pictures/{message.from_user.id}/temp.png")
    massege_cas = await message.answer_photo(types.FSInputFile(path=f"users_pictures/{message.from_user.id}/temp.png"), caption=":)", reply_markup=button_inline)
    print("Кнопка <Получить котика> нажата")
    await state.update_data(cat_mes_id=massege_cas.message_id)


@router.callback_query(F.data == 'Следующий котик')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    media = types.InputMediaPhoto(types.InputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"))
    temp_data = await state.get_data()
    bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_mes_id'])
    
    print("Кнопка <Просмотреть список> нажата")


@router.message(F.text == 'Назад')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_start)
    print("Кнопка <Назад> нажата")