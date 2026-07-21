from buttons import button_list, button_exit_1, list_menu
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import F, Router
from get_cat import get_cat
from init import bot
import shutil
import os


list_router = Router()

class States(StatesGroup):
    waiting_list = State()
    waiting_delete_list = State()


@list_router.callback_query(F.data == 'Списки котиков')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    temp_data = await state.get_data()
    await bot.edit_message_text(text="Выбери что хочешь делать со списками", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_list)
    print("Кнопка <Списки котиков> нажата")


@list_router.callback_query(F.data == 'Добавить список')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    if len(os.listdir(f"users_pictures/{callback.message.from_user.id}/")) >= 99:
            await bot.edit_message_text(text="Достигнут лимит количества списков", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_exit_1)
    else:
        await state.set_state(States.waiting_list)
        temp_data = await state.get_data()
        await bot.edit_message_text(text="Пожалуйста напиши название нового списка", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_exit_1)
        print("Кнопка <Добавить список> нажата")


@list_router.message(States.waiting_list)
async def hello_world(message: Message, state : FSMContext):
    temp_data = await state.get_data()
    await message.delete()
    if str(message.text) not in os.listdir(f"users_pictures/{message.from_user.id}") and "_" not in str(message.text):
        os.makedirs(f"users_pictures/{message.from_user.id}/{message.text}")
        await bot.edit_message_text(text="Выбери что хочешь делать со списками", chat_id=message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_list)
        await state.clear()
        await state.update_data(message_main_id=temp_data['message_main_id'])
    else:
        await bot.edit_message_text(text="Такой список у тебя уже существует или есть _", chat_id=message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_exit_1)


@list_router.callback_query(F.data == 'Отмена_1')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    await state.clear()
    await state.update_data(message_main_id=temp_data['message_main_id'])
    await bot.edit_message_text(text="Выбери что хочешь делать со списками", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_list)
    print("Кнопка <Отмена> нажата")


@list_router.callback_query(F.data == 'Удалить список')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    await bot.edit_message_text(text="Выбери какой список хочешь удалить", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=list_menu(callback.from_user.id, "delete_cat"))
    print("Кнопка <Удалить список> нажата")


@list_router.callback_query(F.data.startswith("delete_cat_list_"))
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    shutil.rmtree(f"users_pictures/{callback.from_user.id}/{callback.data.split("_")[-1]}")
    await bot.edit_message_text(text="Выбери что хочешь делать со списками", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=button_list)
    await state.clear()
    await state.update_data(message_main_id=temp_data['message_main_id'])


@list_router.callback_query(F.data == 'Просмотреть список')
async def hello_world(callback : CallbackQuery, state : FSMContext):
    temp_data = await state.get_data()
    await bot.edit_message_text(text="Вот твои списки", chat_id=callback.message.chat.id, message_id=temp_data['message_main_id'], reply_markup=list_menu(callback.from_user.id, "watch_cat"))
    print("Кнопка <Просмотреть список> нажата")