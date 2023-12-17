from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мои лайки"),
         KeyboardButton(text="Мои альбомы")],
        [KeyboardButton(text="Чарт"),
         KeyboardButton(text="Настройки")
         ]
    ], resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие",
    selective=True
)



rmk = ReplyKeyboardRemove()