from buttons import button_watch_list_cats, button_watch_list_cats_first, button_watch_list_cats_last, button_watch_list_cats_alone
from aiogram.fsm.state import StatesGroup
from aiogram import types
import os


async def choose_keyboard(state : StatesGroup, path_list):
    temp_data = await state.get_data()
    keyboard = button_watch_list_cats
    text = f"{temp_data['picture_number']}/{len(os.listdir(path_list))}"

    if len(os.listdir(path_list)) == 1:
        keyboard = button_watch_list_cats_alone
        text = "1/1"

    elif temp_data['picture_number'] == len(os.listdir(path_list)):
        keyboard = button_watch_list_cats_last
        text = f"{len(os.listdir(path_list))}/{len(os.listdir(path_list))}"

    elif temp_data['picture_number'] == 1:
        keyboard = button_watch_list_cats_first
        text = f"1/{len(os.listdir(path_list))}"

    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number'] - 1]}"), caption=text)

    return keyboard, media


async def choose_keyboard_for_wright_number(state : StatesGroup, path_list, n):
    temp_data = await state.get_data()
    keyboard = button_watch_list_cats
    text = f"{n}/{len(os.listdir(path_list))}"

    if len(os.listdir(path_list)) == 1:
        keyboard = button_watch_list_cats_alone
        text = "1/1"

    elif n == len(os.listdir(path_list)):
        keyboard = button_watch_list_cats_last
        text = f"{len(os.listdir(path_list))}/{len(os.listdir(path_list))}"

    elif n == 1:
        keyboard = button_watch_list_cats_first
        text = f"1/{len(os.listdir(path_list))}"
        
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[n - 1]}"), caption=text)

    return keyboard, media