from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.states import Form
from keyboards import inline, fabrics, reply
from keyboards.reply import rmk
from keyboards.builders import profile
from responses import check_token
from data import DataBase



router = Router()

@router.callback_query(fabrics.Action.filter(F.action.in_('profile')))
async  def fill_profile(call: CallbackQuery, state: FSMContext, bot: Bot):
    await state.set_state(Form.login)
    await bot.send_message(text="✅Первое - введи свой логин Яндекс:", chat_id=call.message.chat.id)


@router.message(Form.login)
async def form_login(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await state.set_state(Form.token)
    await message.answer("✅Теперь нужно ввести токен для авторизации.\n"
                         "Для этого перейдите по одной из ссылок,"
                         "которые находятся ниже и установите расширение либо приложение для Андроид."
                         "Далее нужно пройти процесс авторизации в аккаунт и скопировать в расширении этот токен.", reply_markup=inline.links)

@router.message(Form.token)
async def form_token(message: Message, state: FSMContext):

    if check_token(message.text):

        await state.update_data(token=message.text)
        user_info = await state.get_data()
        print(message.from_user.id, user_info['token'], user_info['login'])
        res = DataBase.add_user(message.from_user.id, user_info['login'], user_info['token'], 2, 192)
        await message.answer("Отлично, теперь давайте перейдем к музыке, выберите что хотите скачать:",
                             reply_markup=reply.main_kb)
        await state.clear()
    else:
        await message.answer("Вы ввели некоректный токен, проверьте его правильность.", reply_markup=fabrics.action_user())
        return
