from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button_start = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Списки котиков", callback_data="Списки котиков")],
                [InlineKeyboardButton(text="Получить котика", callback_data="Получить котика")],
                    ]
)


button_spisok = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Просмотреть список")],
                [KeyboardButton(text="Удалить список"), KeyboardButton(text="Добавить список")],
                [KeyboardButton(text="Назад")],
                    ],
            resize_keyboard=True
)


button_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Следующий котик", callback_data="Следующий котик")],
                [InlineKeyboardButton(text="Добавить котика в список", callback_data="Добавить котика в список")],
                    ]
)