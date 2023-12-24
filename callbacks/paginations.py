import os.path
import random
from yandex_music import ClientAsync, Album
from data import DataBase
from aiogram.fsm.context import FSMContext
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.enums import ChatAction
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from keyboards import fabrics, inline

router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["next", "prev", "down_10_tracks", "down_rand",
                                                               "1-track", "2-track", "3-track", "4-track", "5-track",
                                                               "6-track", "7-track", "8-track",
                                                               "9-track", "10-track"])))
async def pagination_handler_chart(call: CallbackQuery, callback_data: fabrics.Pagination, bot: Bot):
    page_num = int(callback_data.page)
    page = page_num
    token = DataBase.get_token(call.message.chat.id)
    bitrate = int(DataBase.get_bitrate(call.message.chat.id))
    print(call.message.chat.id, token)
    client = await ClientAsync(f'{token}').init()
    track_info = DataBase.get_list_chart_tracks()
    tracks = await client.tracks([str(track_info[i]['track_id']) for i in range(len(track_info))])

    if callback_data.action == "down_10_tracks":
        for i in range(10):
            track = tracks[page * 10 + i]
            track_id = track_info[page * 10 + i]['track_id']
            print(track_id)
            if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', bitrate)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                                filename=f'{" - ".join([track_info[page * 10 + i]["title"], track_info[page * 10 + i]["artist"]])}')
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    for i in range(10):
        if callback_data.action == f"{i + 1}-track":
            track = tracks[page * 10 + i]
            track_id = track_info[page * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', bitrate)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                                filename=f'{" - ".join([track_info[page * 10 + i]["title"], track_info[page * 10 + i]["artist"]])}')
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE,
                                              request_timeout=15)
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "down_rand":
        i_rand = random.randint(0, 100)
        track = tracks[i_rand]
        track_id = track_info[i_rand]['track_id']

        if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
            result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', bitrate)

        audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                            filename=f'{" - ".join([track_info[i_rand]["title"], track_info[i_rand]["artist"]])}')
        bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
        await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "next":
        page = page_num + 1 if page_num < 10 else page_num

    if callback_data.action == "prev":
        page = page_num - 1 if page_num > 0 else 0

    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"🗒️🏆Страница <b>{page + 1}</b>",
                                     reply_markup=fabrics.paginator_chart(page))
    await call.answer()


@router.callback_query(
    fabrics.PaginationTrack.filter(F.action.in_(["next_t", "prev_t", "down_10_tracks_tr", "down_rand_tr",
                                                 "1-track_tr", "2-track_tr", "3-track_tr", "4-track_tr", "5-track_tr",
                                                 "6-track_tr", "7-track_tr", "8-track_tr",
                                                 "9-track_tr", "10-track_tr"])))
async def pagination_handler_likes(call: CallbackQuery, callback_data: fabrics.PaginationTrack, bot: Bot):
    page_num = int(callback_data.page)
    page_now = page_num
    token = DataBase.get_token(call.message.chat.id)
    bitrate = DataBase.get_bitrate(call.message.chat.id)
    print(call.message.chat.id, token)
    client = await ClientAsync(f'{token}').init()
    track_info = DataBase.get_list_select_user_favorite_tracks(call.from_user.id)
    list_title_tracks_likes = [[track['title'], track['artist']] for track in track_info]

    tracks = await client.tracks([str(track_info[i]['track_id']) for i in range(len(track_info))])

    if callback_data.action == "down_10_tracks_tr":
        for i in range(10):
            track = tracks[page_now * 10 + i]

            track_id = track_info[page_now * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
                bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.RECORD_VOICE)
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', bitrate)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                                filename=f'{" - ".join([track_info[page_now * 10 + i]["title"], track_info[page_now * 10 + i]["artist"]])}')
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    for i in range(10):
        if callback_data.action == f"{i + 1}-track_tr":
            track = tracks[page_now * 10 + i]

            track_id = track_info[page_now * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
                bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.RECORD_VOICE)
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', bitrate)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                                filename=f'{" - ".join([track_info[page_now * 10 + i]["title"], track_info[page_now * 10 + i]["artist"]])}')
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "down_rand_tr":
        i_rand = random.randint(0, 100)
        track = tracks[i_rand]
        track_id = track_info[page_now * 10 + i_rand]['track_id']

        if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.RECORD_VOICE)
            result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', bitrate)

        audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                            filename=f'{" - ".join([track_info[page_now * 10 + i_rand]["title"], track_info[page_now * 10 + i_rand]["artist"]])}')
        bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
        await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "next_t":
        page_now = page_num + 1 if page_num < len(track_info) // 10 else page_num

    if callback_data.action == "prev_t":
        page_now = page_now - 1 if page_num >= 1 else 0

    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"🗒️🏆Страница <b>{page_now + 1}</b>",
                                     reply_markup=fabrics.paginator_likes(page_now, list_title_tracks_likes))
    await call.answer()


@router.callback_query(
    fabrics.PaginationAlbum.filter(F.action.in_(["next_a", "prev_a", "1_a", "2_a", "3_a", "4_a", "5_a",
                                                 "6_a", "7_a", "8_a", "9_a"])))
async def pagination_handler_album(call: CallbackQuery, callback_data: fabrics.PaginationAlbum, bot: Bot):
    page_num = int(callback_data.page)
    page_now = page_num
    token = DataBase.get_token(call.message.chat.id)

    print(call.message.chat.id, token)
    client = await ClientAsync(f'{token}').init()
    albums_info = DataBase.get_list_albums(call.from_user.id)
    list_title_artist_album = [[album['title'], album['artist']] for album in albums_info]

    # tracks = await client.tracks([str(albums_info[i]['track_id']) for i in range(len(albums_info))])
    for i in range(9):
        if callback_data.action == f"{i + 1}_a":
            list_tracks = DataBase.get_tracks_from_album(albums_info[i + page_now * 9]['album_id'])

            print(list_tracks)
            album = Album(int(albums_info[i + page_now * 9]['album_id']))
            # photo = await album.download_cover_async(filename=rf"E:\музыка\covers\{albums_info[i + page_now * 9]['album_id']}.jpg"),  photo=rf"E:\музыка\covers\{albums_info[i + page_now * 9]['album_id']}.jpg" ,
            await bot.send_message(chat_id=call.message.chat.id,
                                   text=f"🗒️💽Альбом: <b>{list_title_artist_album[i + page_now * 9][0]} - {list_title_artist_album[i + page_now * 9][1]} </b>\n"
                                        f"Выберите трек, который хотите скачать из этого альбома:",
                                   reply_markup=fabrics.paginator_tracks(0, list_tracks, i + page_now * 9))

    if callback_data.action == "next_a":
        page_now = page_num + 1 if page_num < len(albums_info) // 10 else page_num

    if callback_data.action == "prev_a":
        page_now = page_now - 1 if page_num >= 1 else 0

    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"💽<b>Альбомы из вашей библиотеки</b>\n"
                                     f"🗒️Страница <b>{page_now + 1}</b>",
                                     reply_markup=fabrics.paginator_albums(page_now, list_title_artist_album))
    await call.answer()


@router.callback_query(
    fabrics.PaginationTrackAlbum.filter(F.action.in_(["next_", "prev_", "down_all_tracks_t", "down_rand_t", "back"] + [
        f"{i + 1}-track_t" for i in range(100)])))
async def pagination_handler_tracks(call: CallbackQuery, callback_data: fabrics.PaginationTrackAlbum, bot: Bot):
    page_num = int(callback_data.page)
    page_now = page_num
    token = DataBase.get_token(call.message.chat.id)
    bitrate = DataBase.get_bitrate(call.message.chat.id)
    print(call.message.chat.id, token)
    client = await ClientAsync(f'{token}').init()
    list_tracks = DataBase.get_tracks_from_album(
        DataBase.get_list_albums(call.from_user.id)[callback_data.id_album]['album_id'])

    tracks = await client.tracks([str(list_tracks[i]['track_id']) for i in range(len(list_tracks))])

    if callback_data.action == "down_all_tracks_t":
        for i in range(len(list_tracks)):
            track = tracks[page_now * 10 + i]

            track_id = list_tracks[page_now * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
                bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.RECORD_VOICE)
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', 320)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                                filename=f'{" - ".join([list_tracks[page_now * 10 + i]["title"], list_tracks[page_now * 10 + i]["artist"]])}')
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    for i in range(len(list_tracks)):
        if callback_data.action == f"{i + 1}-track_t":
            track = tracks[page_now * 10 + i]

            track_id = list_tracks[page_now * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
                bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.RECORD_VOICE)
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', 320)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                                filename=f'{" - ".join([list_tracks[page_now * 10 + i]["title"], list_tracks[page_now * 10 + i]["artist"]])}')
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "down_rand_t":
        i_rand = random.randint(0, len(list_tracks))
        track = tracks[i_rand]
        track_id = list_tracks[page_now * 10 + i_rand]['track_id']

        if os.path.exists(rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3') == 0:
            bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.RECORD_VOICE)
            result = await track.download_async(rf"E:\музыка\tracks\{track_id}_{bitrate}.mp3", 'mp3', 320)

        audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}_{bitrate}.mp3',
                            filename=f'{" - ".join([list_tracks[page_now * 10 + i_rand]["title"], list_tracks[page_now * 10 + i_rand]["artist"]])}')
        bool = await bot.send_chat_action(chat_id=call.message.chat.id, action=ChatAction.UPLOAD_VOICE)
        await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    with suppress(TelegramBadRequest):
        if callback_data.action == "back":
            list_album_tuple = DataBase.get_list_albums(call.message.chat.id)
            list_album = [[album['title'], album['artist']] for album in list_album_tuple]
            await call.message.edit_text(f"💽Вот ваши альбомы:\n🗒️🏆Страница <b>{page_now + 1}</b>",
                                         reply_markup=fabrics.paginator_albums(page_now, list_album))
        else:
            await call.message.edit_text(f"🗒️🏆Вот все треки из альбома:</b>",
                                         reply_markup=fabrics.paginator_tracks(page_now, list_tracks,
                                                                               callback_data.id_album))
    await call.answer()


@router.callback_query(fabrics.Action.filter(F.action.in_("no_action")))
async def no_action_button(call: CallbackQuery, callback_data: fabrics.Action, bot: Bot, state: FSMContext):
    if callback_data.action == "no_action":
        await call.message.edit_text("Хорошо, тогда у вас нет доступа к своей музыке,"
                                     "но есть доступ к топ-100 чарту.")
        await state.clear()
    await call.answer()


@router.callback_query(F.data.in_(["backup", "bitrate", "192", "320"]))
async def back_up(call: CallbackQuery):
    if call.data == 'backup':
        res = DataBase.export_csv_albums()
        res2 = DataBase.export_csv_tracks()
        res3 = DataBase.export_csv_users()
        res4 = DataBase.doDump(r'C:\Users\Dmitriy\PycharmProjects\YandexMusicParser\backup\backup.zip')
        await call.message.edit_text("Готово! Файлы сохранены.")
    if call.data == 'bitrate':
        await call.message.edit_text("Выберите теперь битрейт:", reply_markup=inline.bitrate)

    if call.data == '192':
        res = DataBase.update_user_bitratre(call.from_user.id, 192)
        await call.message.edit_text("Готово! Битрейт сохранен.")
    if call.data == '320':
        res = DataBase.update_user_bitratre(call.from_user.id, 320)
        await call.message.edit_text("Готово! Битрейт сохранен.")
