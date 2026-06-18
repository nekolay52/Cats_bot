from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup
import os


def text_for_buttons(user_id):
    user_lisr = os.listdir(f"users_pictures/{user_id}")

    end_list = []
    for i in user_lisr:
        if i != "temp.png":
            end_list.append(i)

    list = []
    for i in range(0, len(end_list)):
        list.append([InlineKeyboardButton(text=end_list[i], callback_data=end_list[i])])

    list.append([InlineKeyboardButton(text="Назад", callback_data="Вернуться к списку кнопок")])

                   
    buttons = InlineKeyboardMarkup(
        inline_keyboard=list,
    )


    return buttons
