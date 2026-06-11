from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
import os


def text_for_buttons(main_list):
    list = []
    for i in range(0, len(main_list)):
        list.append([InlineKeyboardButton(text=main_list[i], callback_data=main_list[i])])
                   
    buttons = InlineKeyboardMarkup(
        inline_keyboard=list
    )

    return buttons
