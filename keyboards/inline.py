from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

links = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Расширение Chrome",
                                 url='https://chrome.google.com/webstore/detail/yandex-music-token/lcbjeookjibfhjjopieifgjnhlegmkib'),
            InlineKeyboardButton(text="Расширение Mozilla",
                                 url='https://addons.mozilla.org/en-US/firefox/addon/yandex-music-token/'),
            InlineKeyboardButton(text="Приложение для Андроид", url='https://disk.yandex.ru/d/aFUXDggXveGaWg')

        ]

    ]

)
