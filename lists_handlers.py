from aiogram import F, Router
from aiogram.filters import Command
from butt import button_start, button_spisok, button_inline
from aiogram.types import Message, CallbackQuery
from tools import get_directory_tree
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from get_cat import get_cat
from aiogram import types
from init import bot
import os


list_router = Router()


class States(StatesGroup):
    waiting_spespopek = State()



@list_router.message(F.text == 'Списки котиков')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Списки котиков> нажата")


@list_router.message(F.text == 'Добавить список')
async def hello_world(message, state: FSMContext):
    await state.set_state(States.waiting_spespopek)
    await message.answer("pls werete youre name ofe spesok", reply_markup=button_spisok)
    print("Кнопка <Добавить список> нажата")

@list_router.message(States.waiting_spespopek)
async def process_name(message, state: FSMContext):
    if str(message.text) not in os.listdir(f"users_pictures/{message.from_user.id}"):
        os.makedirs(f"users_pictures/{message.from_user.id}/{message.text}")
        await message.answer(":)", reply_markup=button_spisok)
    else:
        await message.answer("youre papke ne sozdano", reply_markup=button_spisok)

@list_router.message(F.text == 'Удалить список')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Удалить список> нажата")

@list_router.message(F.text == 'Просмотреть список')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_spisok)
    print("Кнопка <Просмотреть список> нажата")