from aiogram.types import Message
from aiogram import Router
from data import DataBase
from keyboards import fabrics

router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    print(msg)
    user_id = message.from_user.id
    role = DataBase.get_user_role(user_id)
    list_favorite_tracks_user_tuple = DataBase.get_list_select_user_favorite_tracks(user_id)
    list_title_tracks_likes = [[track['title'], track['artist']] for track in list_favorite_tracks_user_tuple]
    # login = DataBase.get_user_login(user_id)

    if msg == 'мои лайки' and (role == 1 or role == 2):
        print(user_id, role)



        await message.answer("Вот 10 треков, которые вам понравились чтобы увидеть следующие или предыдущие, "
                             "воспользуйтесь стрелками.\n💿Страница 1:\n",
                             reply_markup=fabrics.paginator_likes(0, list_title_tracks_likes))
    elif msg == "мои альбомы":
        await message.answer("Вот 10 альбомов, которые вам понравились чтобы увидеть следующие или предыдущие, "
                             "воспользуйтесь стрелками.\n💽Страница 1:\n", reply_markup=fabrics.paginator_albums())
    elif msg == 'чарт':
        res = DataBase.update_chart_list()

        await message.answer('Вот 10 треков чарта, чтобы увидеть следующие или предыдущие, '
                             'воспользуйтесь стрелками.\n🗒️🏆Страница 1:\n',
                             reply_markup=fabrics.paginator_chart())

    else:
        await message.answer("Я не понял сообщение.")
