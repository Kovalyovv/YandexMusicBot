from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Расширение Chrome",
                                 url='https://chrome.google.com/webstore/detail/yandex-music-token/lcbjeookjibfhjjopieifgjnhlegmkib'),
            InlineKeyboardButton(text="Авторизация через Яндекс",
                                 url='https://oauth.yandex.ru/authorize?response_type=token&client_id=30075430e32543be905c1d7c76a5515d'),
            InlineKeyboardButton(text="Приложение для Андроид", url='https://disk.yandex.ru/d/aFUXDggXveGaWg'),
        ], [InlineKeyboardButton(text="❌Не хочу писать токен", callback_data="no_action")]

    ]

)


bitrate = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="192 кбит/с", callback_data="192"),
            InlineKeyboardButton(text="320 кбит/с", callback_data="320")
        ]
    ]
)


admin = InlineKeyboardMarkup(
inline_keyboard=[
        [
            InlineKeyboardButton(text="Сделать бэкап", callback_data="backup"),
            InlineKeyboardButton(text="Поменять битрейт", callback_data="bitrate")
        ]
    ]

)