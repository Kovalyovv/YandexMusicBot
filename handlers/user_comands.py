import random
from keyboards import fabrics
from aiogram import Router, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from keyboards import reply
from data.DataBase import is_user, update_favorite_tracks, delete_user

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    if is_user(message.from_user.id):
        await message.answer(f"<b>Привет, {message.from_user.first_name}</b>, с возвращением!\nОбновляю твою библиотеку, подожди немного. Как закончу, дам знать.\n")
        res = update_favorite_tracks(message.from_user.id)
        await message.answer("Готово, выбери любую команду ниже⬇️.", reply_markup=reply.main_kb)
    else:
        await message.answer(f"<b>Привет, {message.from_user.first_name}!</b>\n"
                         f"Я музыкальный бот, который поможет тебе скачать любимые треки "
                         f"или альбомы из твоей библиотеки Яндекс Музыки.", reply_markup=fabrics.user_info())

@router.message(Command('restart'))
async def restart(message: Message):
    if is_user(message.from_user.id):
        res = delete_user(message.from_user.id)
    res2 = await start(message)

@router.message(Command(commands=['rn', "random_number"]))
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(x) for x in command.args.split("-")]
    rnum = random.randint(a, b)
    await message.reply(f"Random number: {rnum}")

