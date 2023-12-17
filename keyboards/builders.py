from typing import Union

from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def profile(text: Union[str, list]):
    builder = ReplyKeyboardBuilder()

    if isinstance(text, str):
        text = [text]

    [builder.button(text= txt) for txt in text]
    return builder.as_markup(resize_keyboard=True, one_time_keyborad=True)

