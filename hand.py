from aiogram import F, Router
from aiogram.filters import Command
from butt import button_start, button_spisok


router = Router()


@router.message(Command('start'))
async def hello_world(message):
    await message.answer("О привет! Выбери пожалуйста что ты хочешь делать :)", reply_markup=button_start)
    print("Кнопка <start> нажата")


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
    await message.answer(":)")
    print("Кнопка <Получить котика> нажата")


@router.message(F.text == 'Назад')
async def hello_world(message):
    await message.answer(":)", reply_markup=button_start)
    print("Кнопка <Назад> нажата")

