from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from configs import CATEGORIES


def button_category():
    buttons = []

    for category in CATEGORIES.keys():
        buttons.append([KeyboardButton(text=category)])



    markup = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
         one_time_keyboard=False
    )
    return markup
