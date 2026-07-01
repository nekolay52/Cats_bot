from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os


button_main_menu = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Списки котиков", callback_data="Списки котиков", style="primary")],
                [InlineKeyboardButton(text="Получить котика", callback_data="Получить котика", style="success")],
                    ]
)


button_list = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Просмотреть список", callback_data="Просмотреть список", style="primary")],
                [InlineKeyboardButton(text="Удалить список", callback_data="Удалить список", style="danger")],
                [InlineKeyboardButton(text="Добавить список", callback_data="Добавить список", style="success")],
                [InlineKeyboardButton(text="Назад", callback_data="Назад")],
                    ]
)


button_watch_cats = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Следующий котик", callback_data="Следующий котик", style="primary")],
                [InlineKeyboardButton(text="Добавить котика в список", callback_data="Добавить котика в список", style="success")],
                    ]
)


button_exit = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Отмена", callback_data="Отмена", style="danger")]
                    ]
)


def add_cat_list_menu(user_id):
    user_lisr = os.listdir(f"users_pictures/{user_id}")

    end_list = []
    for i in user_lisr:
        if i != "temp.png":
            end_list.append(i)

    list = []
    for i in range(0, len(end_list)):
        list.append([InlineKeyboardButton(text=end_list[i], callback_data=f"add_cat_list_{end_list[i]}")])

    list.append([InlineKeyboardButton(text="Назад", callback_data="Вернуться к списку кнопок")])

                   
    buttons = InlineKeyboardMarkup(
        inline_keyboard=list,
    )

    return buttons


def delete_cat_list_menu(user_id):
    user_lisr = os.listdir(f"users_pictures/{user_id}")

    end_list = []
    for i in user_lisr:
        if i != "temp.png":
            end_list.append(i)

    list = []
    for i in range(0, len(end_list)):
        list.append([InlineKeyboardButton(text=end_list[i], callback_data=f"delete_cat_list_{end_list[i]}")])

    list.append([InlineKeyboardButton(text="Назад", callback_data="Вернуться к списку кнопок")])

                   
    buttons = InlineKeyboardMarkup(
        inline_keyboard=list,
    )

    return buttons

def append_in_cat_list_menu(user_id):
    user_lisr = os.listdir(f"users_pictures/{user_id}")

    end_list = []
    for i in user_lisr:
        if i != "temp.png":
            end_list.append(i)

    list = []
    for i in range(0, len(end_list)):
        list.append([InlineKeyboardButton(text=end_list[i], callback_data=f"append_in_cat_list_{end_list[i]}")])

    list.append([InlineKeyboardButton(text="Назад", callback_data="Вернуться в свайп котов")])

                   
    buttons = InlineKeyboardMarkup(
        inline_keyboard=list,
    )

    return buttons