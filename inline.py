from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
import os


def inline(spis_spiskov):
    yuy = []
    for i in range(0, len(spis_spiskov)):
        yuy.append([InlineKeyboardButton(text=spis_spiskov[i], callback_data=spis_spiskov[i])])
                   
    inline_test = InlineKeyboardMarkup(
        inline_keyboard=yuy
    )

    return inline_test

# print(os.listdir(f"users_pictures/6221228152"))
# print(inline(os.listdir(f"users_pictures/6221228152")))