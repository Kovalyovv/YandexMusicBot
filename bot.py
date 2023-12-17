from yandex_music import ClientAsync, Playlist, track_short
import yandex_music.utils.request_async

import asyncio

from aiogram import Bot, Dispatcher, F

from pprint import pprint
from handlers import bot_messages, user_comands, questionnaire
from callbacks import paginations
from config_reader import config

async def main():
    bot = Bot(config.bot_token.get_secret_value(), parse_mode="HTML")
    dp = Dispatcher()
    dp.include_routers(
        user_comands.router,
        paginations.router,
        questionnaire.router,
        bot_messages.router

    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
