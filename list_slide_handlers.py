from buttons import button_watch_list_cats, list_menu, button_exit_2
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from aiogram import types
from init import bot
import os


list_slide_router = Router()

class States(StatesGroup):
    waiting_number = State()
    

@list_slide_router.callback_query(F.data.startswith("watch_cat_list_"))
async def hello_world(callback : CallbackQuery, state : FSMContext):
    path_list = f"users_pictures/{callback.from_user.id}/{callback.data.split("_")[-1]}"
    if os.listdir(path_list) != []:
        media = await callback.message.answer_photo(types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[0]}"), caption=f"1 / {len(os.listdir(path_list))}", reply_markup=button_watch_list_cats)
        await state.update_data(cat_slide_message_id=media.message_id)
        await state.update_data(picture_number=1)
        await state.update_data(directory=callback.data.split("_")[-1])
    else:
        temp_data = await state.get_data()
        await bot.edit_message_text(text="Данный список пуст", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=list_menu(callback.from_user.id, "watch_cat"))


@list_slide_router.callback_query(F.data == "вправо")
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    path_list = f"users_pictures/{callback.from_user.id}/{temp_data['directory']}"
    if temp_data['picture_number'] != len(os.listdir(path_list)):
        media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number']]}"), caption=f"{temp_data['picture_number'] + 1} / {len(os.listdir(path_list))}")
        await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_slide_message_id'], reply_markup=button_watch_list_cats)
        await state.update_data(picture_number=temp_data['picture_number'] + 1)
    else:
        pass
    print("Кнопка <вправо> нажата")


@list_slide_router.callback_query(F.data == "влево")
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    path_list = f"users_pictures/{callback.from_user.id}/{temp_data['directory']}"
    if temp_data['picture_number'] > 1:
        media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number'] - 2]}"), caption=f"{temp_data['picture_number'] - 1} / {len(os.listdir(path_list))}")
        await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_slide_message_id'], reply_markup=button_watch_list_cats)
        await state.update_data(picture_number=temp_data['picture_number'] - 1)
    else:
        pass
    print("Кнопка <влево> нажата")


@list_slide_router.callback_query(F.data == 'Ввести номер')
async def hello_world(callback : CallbackQuery, state: FSMContext):
    await state.set_state(States.waiting_number)
    input_cat_number = await callback.message.answer(text="Пожалуйста напиши номер фотки", reply_markup=button_exit_2)
    await state.update_data(input_cat_number_id=input_cat_number.message_id)
    print("Кнопка <Ввести номер> нажата")


@list_slide_router.message(States.waiting_number)
async def hello_world(message : Message, state: FSMContext):
    await message.delete()
    temp_data = await state.get_data()
    path_list = f"users_pictures/{message.from_user.id}/{temp_data['directory']}"
    if message.text.isdigit() == False:
        await bot.edit_message_text(text="Пожалуйста введите корректное число", chat_id=message.chat.id, message_id=temp_data['input_cat_number_id'], reply_markup=button_exit_2)
    else:
        if int(message.text) < 1 or int(message.text) > len(os.listdir(path_list)):
            await bot.edit_message_text(text="Пожалуйста введите корректное число", chat_id=message.chat.id, message_id=temp_data['input_cat_number_id'], reply_markup=button_exit_2)
        else:
            media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[int(message.text) - 1]}"), caption=f"{int(message.text)} / {len(os.listdir(path_list))}")
            await bot.edit_message_media(media=media, chat_id=message.chat.id, message_id=temp_data['cat_slide_message_id'], reply_markup=button_watch_list_cats)
            await state.update_data(picture_number=int(message.text))
            await bot.delete_message(chat_id=message.chat.id, message_id=temp_data['input_cat_number_id'])
            temp_data.pop("input_cat_number_id")
            await state.set_data(temp_data)


@list_slide_router.callback_query(F.data == 'Отмена_2')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    await state.set_state(None)
    temp_data = await state.get_data()
    await callback.message.delete()
    temp_data.pop("input_cat_number_id")
    await state.set_data(temp_data)
    print("Кнопка <Отмена> нажата")


@list_slide_router.callback_query(F.data == "Удалить фото")
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    path_list = f"users_pictures/{callback.from_user.id}/{temp_data['directory']}"
    if len(os.listdir(path_list)) == 1:
        pass
    else:
        os.remove(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number'] - 1]}")
        if temp_data['picture_number'] == 1:
            media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number'] - 1]}"), caption=f"{temp_data['picture_number']} / {len(os.listdir(path_list))}")
            await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_slide_message_id'], reply_markup=button_watch_list_cats)
            await state.update_data(picture_number=temp_data['picture_number'])
        else:
            media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number'] - 2]}"), caption=f"{temp_data['picture_number'] - 1} / {len(os.listdir(path_list))}")
            await bot.edit_message_media(media=media, chat_id=callback.message.chat.id, message_id=temp_data['cat_slide_message_id'], reply_markup=button_watch_list_cats)
            await state.update_data(picture_number=temp_data['picture_number'] - 1)
    print("Кнопка <Удалить фото> нажата")


@list_slide_router.callback_query(F.data == 'Закрыть_2')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=temp_data['cat_slide_message_id'])
    temp_data.pop("cat_slide_message_id")
    await state.set_data(temp_data)
    print("Кнопка <Закрыть> нажата")