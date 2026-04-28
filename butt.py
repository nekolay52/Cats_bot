from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button_start = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Списки котиков")],
                [KeyboardButton(text="Получить котика")],
                    ],
            resize_keyboard=True
)


button_spisok = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Просмотреть список")],
                [KeyboardButton(text="Удалить список"), KeyboardButton(text="Добавить список")],
                [KeyboardButton(text="Назад")],
                    ],
            resize_keyboard=True
)

