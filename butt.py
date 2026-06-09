from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


button_start = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Списки котиков", callback_data="Списки котиков")],
                [InlineKeyboardButton(text="Получить котика", callback_data="Получить котика")],
                    ]
)


button_spisok = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Просмотреть список", callback_data="Просмотреть список")],
                [InlineKeyboardButton(text="Удалить список", callback_data="Удалить список")],
                [InlineKeyboardButton(text="Добавить список", callback_data="Добавить список")],
                [InlineKeyboardButton(text="Назад", callback_data="Назад")],
                    ]
)


button_inline = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Следующий котик", callback_data="Следующий котик")],
                [InlineKeyboardButton(text="Добавить котика в список", callback_data="Добавить котика в список")],
                    ]
)