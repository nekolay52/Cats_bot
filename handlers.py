from buttons import button_main_menu, button_list, button_watch_cats, append_in_cat_list_menu
from aiogram.types import CallbackQuery
from tools import get_directory_tree
from aiogram.filters import Command
from aiogram import F, Router
from get_cat import get_cat
from aiogram import types
from init import bot
import shutil
import os


router = Router()


@router.message(Command('start'))
async def hello_world(message, state):
    if str(message.from_user.id) not in os.listdir("users_pictures"):
        os.makedirs(f"users_pictures/{message.from_user.id}")
    messege_main = await message.answer("О привет! Выбери пожалуйста что ты хочешь делать", reply_markup=button_main_menu)
    await state.update_data(messege_main_id=messege_main.message_id)
    print("Команда <start> введена")


@router.message(Command('info'))
async def hello_world(message):
    directory_tree = get_directory_tree("./")
    await message.answer(f"```\n{directory_tree}\n```", parse_mode="Markdown")
    print("Команда <info> введена")


@router.callback_query(F.data == 'Получить котика')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    media = await callback.message.answer_photo(types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption="Котик", reply_markup=button_watch_cats)
    await state.update_data(cat_massege_id=media.message_id)
    print("Кнопка <Получить котика> нажата")


@router.callback_query(F.data == 'Следующий котик')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption="Котик")
    temp_data = await state.get_data()
    await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_massege_id'], reply_markup=button_watch_cats)
    print("Кнопка <Следующий котик> нажата")


@router.callback_query(F.data == 'Добавить котика в список')
async def hello_world(callback : CallbackQuery, state):
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption="Котик")
    temp_data = await state.get_data()
    await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_massege_id'], reply_markup=append_in_cat_list_menu(callback.from_user.id))
    print("Кнопка <Добавить котика в список> нажата")


@router.callback_query(F.data.startswith("append_in_cat_list_"))
async def hello_world(callback : CallbackQuery, state):
    name_dir = os.listdir(f"users_pictures/{callback.from_user.id}/{callback.data.split("_")[-1]}")
    count = 0
    if len(name_dir) == 0:
        shutil.copy(src=f"users_pictures/{callback.from_user.id}/temp.png", dst=f"users_pictures/{callback.from_user.id}/{callback.data.split("_")[-1]}/{"0"}.png")
    else:
        for i in name_dir:
            if int(i.split(".")[0]) > count:
                count = int(i.split(".")[0])
        shutil.copy(src=f"users_pictures/{callback.from_user.id}/temp.png", dst=f"users_pictures/{callback.from_user.id}/{callback.data.split("_")[-1]}/{count + 1}.png")
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption="Котик")
    temp_data = await state.get_data()
    await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_massege_id'], reply_markup=button_watch_cats)


@router.callback_query(F.data == 'Назад')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    temp_data = await state.get_data()
    await bot.edit_message_text(text="О привет! Выбери пожалуйста что ты хочешь делать", chat_id=callback.message.chat.id, message_id=temp_data['messege_main_id'], reply_markup=button_main_menu)
    print("Кнопка <Назад> нажата")


@router.callback_query(F.data == 'Вернуться к списку кнопок')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    temp_data = await state.get_data()
    await bot.edit_message_text(text="Выбери что хочешь делать со списками", chat_id=callback.message.chat.id, message_id=temp_data['messege_main_id'], reply_markup=button_list)
    print("Кнопка <Назад> нажата")


@router.callback_query(F.data == 'Вернуться в свайп котов')
async def hello_world(callback : CallbackQuery, state):
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"users_pictures/{callback.from_user.id}/temp.png"), caption="Котик")
    temp_data = await state.get_data()
    await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_massege_id'], reply_markup=button_watch_cats)
    print("Кнопка <Назад> нажата")

