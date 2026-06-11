from aiogram import F, Router
from aiogram.filters import Command
from buttons import button_start, button_list, button_watch_cats
from aiogram.types import Message, CallbackQuery
from tools import get_directory_tree
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from get_cat import get_cat
from aiogram import types
from text_for_buttons import text_for_buttons
from init import bot
import os


list_router = Router()

class States(StatesGroup):
    waiting_spespopek = State()


@list_router.callback_query(F.data == 'Списки котиков')
async def hello_world(callback : CallbackQuery, state):
    get_cat(f"users_pictures/{callback.from_user.id}/temp.png")
    temp_data = await state.get_data()
    await bot.edit_message_text(text="Выбери что хочешь делать со списками", chat_id=callback.message.chat.id, message_id=temp_data['messege_main_id'], reply_markup=button_list)
    print("Кнопка <Списки котиков> нажата")


@list_router.callback_query(F.text == 'Добавить список')
async def hello_world(callback : CallbackQuery, state: FSMContext):
    await state.set_state(States.waiting_spespopek)
    await callback.message.answer("Пожалуйста напиши название нового списка", reply_markup=button_list)
    print("Кнопка <Добавить список> нажата")


@list_router.callback_query(States.waiting_spespopek)
async def process_name(callback : CallbackQuery, state: FSMContext):
    if str(callback.message.text) not in os.listdir(f"users_pictures/{callback.message.from_user.id}"):
        os.makedirs(f"users_pictures/{callback.message.from_user.id}/{callback.message.text}")
        await callback.message.answer("Такой список у тебя уже существует", reply_markup=button_list)
        await state.clear()
    else:
        await callback.message.answer("Такой список у тебя уже существует", reply_markup=button_list)

@list_router.callback_query(F.text == 'Удалить список')
async def hello_world(message):
    await message.answer("Выбери какой список хочешь удалить", reply_markup=button_list)
    print("Кнопка <Удалить список> нажата")


@list_router.callback_query(F.text == 'Просмотреть список')
async def hello_world(message):
    await message.answer("Вот твои списки", reply_markup=text_for_buttons(os.listdir(f"users_pictures/{message.from_user.id}")))
    print("Кнопка <Просмотреть список> нажата")
