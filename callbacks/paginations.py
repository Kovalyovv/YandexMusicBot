import os.path
import random
import random
from yandex_music import ClientAsync
from data import DataBase
from aiogram import Bot, F, Router
from aiogram.types import CallbackQuery, FSInputFile
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from keyboards import fabrics

router = Router()


@router.callback_query(fabrics.Pagination.filter(F.action.in_(["next", "prev", "down_10_tracks", "down_rand",
                                                               "1-track", "2-track", "3-track", "4-track", "5-track",
                                                               "6-track", "7-track", "8-track",
                                                               "9-track", "10-track"])))
async def pagination_handler_chart(call: CallbackQuery, callback_data: fabrics.Pagination, bot: Bot):
    page_num = int(callback_data.page)
    page = page_num
    token = DataBase.get_token(call.message.chat.id)
    print(call.message.chat.id, token)
    client = await ClientAsync(f'{token}').init()
    track_info = DataBase.get_list_chart_tracks()
    tracks = await client.tracks([str(track_info[i]['track_id']) for i in range(len(track_info))])

    if callback_data.action == "down_10_tracks":
        for i in range(10):
            track = tracks[page * 10 + i]
            track_id = track_info[page * 10 + i]['track_id']
            print(track_id)
            if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}.mp3", 'mp3', 320)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}.mp3',
                                filename=f'{" - ".join([track_info[page * 10 + i]["title"], track_info[page * 10 + i]["artist"]])}')
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    for i in range(10):
        if callback_data.action == f"{i+1}-track":
            track = tracks[page * 10 + i]
            track_id = track_info[page * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}.mp3", 'mp3', 320)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}.mp3',
                                filename=f'{" - ".join([track_info[page * 10 + i]["title"], track_info[page * 10 + i]["artist"]])}')
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "down_rand":
        i_rand = random.randint(0,100)
        track = tracks[i_rand]
        track_id = track_info[i_rand]['track_id']

        if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
            result = await track.download_async(rf"E:\музыка\tracks\{track_id}.mp3", 'mp3', 320)

        audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}.mp3',
                            filename=f'{" - ".join([track_info[i_rand]["title"], track_info[i_rand]["artist"]])}')
        await bot.send_audio(chat_id=call.message.chat.id, audio=audio)


    if callback_data.action == "next":
        page = page_num + 1 if page_num < 10 else page_num

    if callback_data.action == "prev":
        page = page_num - 1 if page_num > 0 else 0

    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"🗒️🏆Страница <b>{page + 1}</b>",
                                     reply_markup=fabrics.paginator_chart(page))
    await call.answer()



@router.callback_query(fabrics.Pagination.filter(F.action.in_(["next_tr", "prev", "down_10_tracks_tr", "down_rand_tr",
                                                               "1-track_tr", "2-track_tr", "3-track_tr", "4-track_tr", "5-track_tr",
                                                               "6-track_tr", "7-track_tr", "8-track_tr",
                                                               "9-track_tr", "10-track_tr"])))
async def pagination_handler_chart(call: CallbackQuery, callback_data: fabrics.PaginationTrack, bot: Bot):
    page_num = int(callback_data.page)
    page = page_num
    list_favorite_tracks_user_tuple = DataBase.get_list_favorite_tracks(call.from_user.id)

    token = DataBase.get_token(call.message.chat.id)
    print(call.message.chat.id, token)
    client = await ClientAsync(f'{token}').init()
    track_info = DataBase.get_list_chart_tracks()
    tracks = await client.tracks([str(track_info[i]['track_id']) for i in range(len(track_info))])

    if callback_data.action == "down_10_tracks_tr":
        for i in range(10):
            track = tracks[page * 10 + i]
            track_id = track_info[page * 10 + i]['track_id']
            print(track_id)
            if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}.mp3", 'mp3', 320)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}.mp3',
                                filename=f'{" - ".join([track_info[page * 10 + i]["title"], track_info[page * 10 + i]["artist"]])}')
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    for i in range(10):
        if callback_data.action == f"{i+1}-track_tr":
            track = tracks[page * 10 + i]
            track_id = track_info[page * 10 + i]['track_id']

            if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
                result = await track.download_async(rf"E:\музыка\tracks\{track_id}.mp3", 'mp3', 320)

            audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}.mp3',
                                filename=f'{" - ".join([track_info[page * 10 + i]["title"], track_info[page * 10 + i]["artist"]])}')
            await bot.send_audio(chat_id=call.message.chat.id, audio=audio)

    if callback_data.action == "down_rand_tr":
        i_rand = random.randint(0,100)
        track = tracks[i_rand]
        track_id = track_info[i_rand]['track_id']

        if os.path.exists(rf'E:\музыка\tracks\{track_id}.mp3') == 0:
            result = await track.download_async(rf"E:\музыка\tracks\{track_id}.mp3", 'mp3', 320)

        audio = FSInputFile(path=rf'E:\музыка\tracks\{track_id}.mp3',
                            filename=f'{" - ".join([track_info[i_rand]["title"], track_info[i_rand]["artist"]])}')
        await bot.send_audio(chat_id=call.message.chat.id, audio=audio)


    if callback_data.action == "next_tr":
        page = page_num + 1 if page_num < 10 else page_num

    if callback_data.action == "prev_tr":
        page = page_num - 1 if page_num > 0 else 0

    with suppress(TelegramBadRequest):
        await call.message.edit_text(f"🗒️🏆Страница <b>{page + 1}</b>",
                                     reply_markup=fabrics.paginator_likes(page))
    await call.answer()




@router.callback_query(fabrics.Action.filter(F.action.in_("no_action")))
async def no_action_button(call: CallbackQuery, callback_data: fabrics.Action, bot: Bot):
    if callback_data.action == "no_action":
        await call.message.edit_text("Хорошо, тогда у вас нет доступа к своей музыке,"
                                     "но есть доступ к топ-100 чарту.")
    await call.answer()
