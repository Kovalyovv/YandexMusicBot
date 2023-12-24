from aiogram.types import Message
from aiogram import Router
from data import DataBase
from keyboards import fabrics, inline

router = Router()


@router.message()
async def echo(message: Message):
    msg = message.text.lower()
    print(msg)
    user_id = message.from_user.id
    role = DataBase.get_user_role(user_id)
    print(role)
    # res = DataBase.update_favorite_tracks(user_id)
    list_favorite_tracks_user_tuple = DataBase.get_list_select_user_favorite_tracks(user_id)
    list_title_tracks_likes = [[track['title'], track['artist']] for track in list_favorite_tracks_user_tuple]
    # login = DataBase.get_user_login(user_id)

    if msg == 'мои лайки' and (role == 1 or role == 2):
        if(len(list_title_tracks_likes)== 0):
            DataBase.update_favorite_tracks(message.from_user.id)
        print(user_id, role)
        await message.answer("Вот 10 треков, которые вам понравились чтобы увидеть следующие или предыдущие, "
                             "воспользуйтесь стрелками.\n💿Страница 1:\n",
                             reply_markup=fabrics.paginator_likes(0, list_title_tracks_likes))
    elif msg == 'мои лайки' and role == 3:
        await message.answer("😢К сожалению вам недоступен список треков. Чтобы его получить введите токен.\n/start")
    elif msg == "мои альбомы" and (role == 1 or role == 2):
        await message.answer("Подождите немного, я подгружаю альбомы из вашей библиотеки.💤\n")
        res = DataBase.list_album_update(message.from_user.id)

        list_album_tuple =  DataBase.get_list_albums(message.from_user.id)
        list_album = [[album['title'], album['artist']] for album in list_album_tuple]
        # print(list_album)
        await message.answer("Вот альбомы, которые вам понравились чтобы увидеть следующие или предыдущие, "
                             "воспользуйтесь стрелками.\n💽Страница 1:\n", reply_markup=fabrics.paginator_albums(0, list_album))
    elif msg == 'чарт':
        res = DataBase.update_chart_list()

        await message.answer('Вот 10 треков чарта, чтобы увидеть следующие или предыдущие, '
                             'воспользуйтесь стрелками.\n🗒️🏆Страница 1:\n',
                             reply_markup=fabrics.paginator_chart())
    elif msg == 'настройки' and role == 1:
        await message.answer(
            "Можно сделать бэкап или поменять битрейт🎵.\nВыберите любой из доступных ниже.",
            reply_markup=inline.admin)

    elif msg == 'настройки' and role == 2:
        await message.answer("У вас есть возможность поменять битрейт скачивания трека🎵.\nВыберите любой из доступных ниже.", reply_markup=inline.bitrate)


    else:
        await message.answer("Я не понял сообщение.")
