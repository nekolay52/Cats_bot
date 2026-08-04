from buttons import button_watch_list_cats, button_watch_list_cats_first, button_watch_list_cats_last, button_watch_list_cats_alone
from aiogram.fsm.state import StatesGroup
from aiogram import types
import os


def get_directory_tree(path, show_hidden=False, max_depth=None, current_depth=0, prefix='', is_last_root=True):
    lines = []
    abs_path = os.path.abspath(path)
    root_name = os.path.basename(abs_path) + '\n'

    if current_depth == 0:
        lines.append(root_name)

    if max_depth is not None and current_depth > max_depth:
        return ''.join(lines)

    try:
        entries = sorted(os.listdir(path))
    except PermissionError:
        lines.append(f"{prefix}{'└── ' if is_last_root else '├── '}[Permission Denied]\n")
        return ''.join(lines)

    if not show_hidden:
        entries = [e for e in entries if not e.startswith('.')]

    count = len(entries)
    for idx, entry in enumerate(entries):
        if entry!="__pycache__":
            full_path = os.path.join(path, entry)
            is_last = (idx == count - 1)

            connector = '└── ' if is_last else '├── '
            lines.append(f"{prefix}{connector}{entry}{'/' if os.path.isdir(full_path) else ''}\n")

            if os.path.isdir(full_path):
                new_prefix = prefix + ('    ' if is_last else '│   ')
                subtree = get_directory_tree(
                    full_path,
                    show_hidden=show_hidden,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                    prefix=new_prefix,
                    is_last_root=is_last
                )
                lines.append(subtree)

    return ''.join(lines)


async def choose_keyboard(state : StatesGroup, path_list):
    temp_data = await state.get_data()
    keyboard = button_watch_list_cats
    text = f"{temp_data['picture_number']}/{len(os.listdir(path_list))}"

    if len(os.listdir(path_list)) == 1:
        keyboard = button_watch_list_cats_alone
        text = "1/1"

    elif temp_data['picture_number'] == len(os.listdir(path_list)):
        keyboard = button_watch_list_cats_last
        text = f"{len(os.listdir(path_list))}/{len(os.listdir(path_list))}"

    elif temp_data['picture_number'] == 1:
        keyboard = button_watch_list_cats_first
        text = f"1/{len(os.listdir(path_list))}"

    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[temp_data['picture_number'] - 1]}"), caption=text)

    return keyboard, media


async def choose_keyboard_for_wright_number(state : StatesGroup, path_list, n):
    temp_data = await state.get_data()
    keyboard = button_watch_list_cats
    text = f"{n}/{len(os.listdir(path_list))}"

    if len(os.listdir(path_list)) == 1:
        keyboard = button_watch_list_cats_alone
        text = "1/1"

    elif n == len(os.listdir(path_list)):
        keyboard = button_watch_list_cats_last
        text = f"{len(os.listdir(path_list))}/{len(os.listdir(path_list))}"

    elif n == 1:
        keyboard = button_watch_list_cats_first
        text = f"1/{len(os.listdir(path_list))}"
        
    media = types.InputMediaPhoto(media=types.FSInputFile(path=f"{path_list}/{sorted(os.listdir(path_list))[n - 1]}"), caption=text)

    return keyboard, media