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
                [InlineKeyboardButton(text="Назад", callback_data="Назад_1")],
                    ]
)


button_watch_cats = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Следующий котик", callback_data="Следующий котик", style="primary")],
                [InlineKeyboardButton(text="Добавить котика в список", callback_data="Добавить котика в список", style="success")],
                [InlineKeyboardButton(text="Закрыть", callback_data="Закрыть_1", style="danger")],
                    ]
)


button_watch_list_cats = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="◀️", callback_data="влево", style="primary"), InlineKeyboardButton(text="▶️", callback_data="вправо", style="primary")],
                [InlineKeyboardButton(text="Ввести номер", callback_data="Ввести номер", style="success")],
                [InlineKeyboardButton(text="Удалить фото", callback_data="Удалить фото", style="danger")],
                [InlineKeyboardButton(text="Закрыть", callback_data="Закрыть_2", style="danger")],
                    ]
)


button_exit_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Отмена", callback_data="Отмена_1", style="danger")],
                    ]
)


button_exit_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Отмена", callback_data="Отмена_2", style="danger")],
                    ]
)


def list_menu(user_id, factor):
    user_lisr = os.listdir(f"users_pictures/{user_id}")

    end_list = []
    for i in user_lisr:
        if i != "temp.png":
            end_list.append(i)

    list = []
    for i in range(0, len(end_list)):
        list.append([InlineKeyboardButton(text=end_list[i], callback_data=f"{factor}_list_{end_list[i]}")])

    if factor == "delete_cat" or factor == "watch_cat":
        list.append([InlineKeyboardButton(text="Назад", callback_data="Назад_2")])

    if factor == "append_in_cat":
        list.append([InlineKeyboardButton(text="Назад", callback_data="Назад_3")])
        
    buttons = InlineKeyboardMarkup(
        inline_keyboard=list,
    )

    return buttons