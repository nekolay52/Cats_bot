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
async def hello_world(message, state):
    if str(message.from_user.id) not in os.listdir("users_pictures"):
        os.makedirs(f"users_pictures/{message.from_user.id}")
    messege_main = await message.answer("О привет! Выбери пожалуйста что ты хочешь делать :)", reply_markup=button_start)
    print("Кнопка <start> нажата")
    await state.update_data(messege_main_id=messege_main.message_id)


@router.message(Command('info'))
async def hello_world(message):
    l = get_directory_tree("./")
    await message.answer(f"```\n{l}\n```", reply_markup=button_start, parse_mode="Markdown")
    print("Кнопка <info> нажата")


@router.callback_query(F.data == 'Получить котика')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    massege_cas = await callback.message.answer_photo(types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption=":)", reply_markup=button_inline)
    print("Кнопка <Получить котика> нажата")
    await state.update_data(cat_mes_id=massege_cas.message_id)


@router.callback_query(F.data == 'Следующий котик')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption=":)")
    temp_data = await state.get_data()
    await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_mes_id'], reply_markup=button_inline)
    print("Кнопка <Просмотреть список> нажата")


@router.callback_query(F.data == 'Назад')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    temp_data = await state.get_data()
    await bot.edit_message_text(text=":)", chat_id=callback.message.chat.id, message_id=temp_data['messege_main_id'], reply_markup=button_spisok)
    print("Кнопка <Назад> нажата")