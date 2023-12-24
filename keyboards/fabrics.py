from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from data import DataBase



class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int


class PaginationTrack(CallbackData, prefix="pag_tr"):
    action: str
    page: int

class PaginationTrackAlbum(CallbackData, prefix="pag_tr"):
    action: str
    page: int
    count: int
    id_album: int

class PaginationAlbum(CallbackData, prefix="pag_a"):
    action: str
    page: int

class Action(CallbackData, prefix="act"):
    action: str


list_title_tracks_chart = [[track['title'], track['artist']] for track in DataBase.get_list_chart_tracks()]


def paginator_chart(page: int = 0):
    track_kb = InlineKeyboardBuilder()
    track_kb.row(
        InlineKeyboardButton(text="⬇️Скачать 10 треков",
                             callback_data=Pagination(action="down_10_tracks", page=page).pack()),
        InlineKeyboardButton(text="⬇️Скачать рандомный",
                             callback_data=Pagination(action="down_rand", page=page).pack()),
        width=2
    )
    track_kb.row(
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10])}',
                             callback_data=Pagination(action='1-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 1])}',
                             callback_data=Pagination(action='2-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 2])}',
                             callback_data=Pagination(action='3-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 3])}',
                             callback_data=Pagination(action='4-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 4])}',
                             callback_data=Pagination(action='5-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 5])}',
                             callback_data=Pagination(action='6-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 6])}',
                             callback_data=Pagination(action='7-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 7])}',
                             callback_data=Pagination(action='8-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 8])}',
                             callback_data=Pagination(action='9-track', page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_chart[page * 10 + 9])}',
                             callback_data=Pagination(action='10-track', page=page).pack()),
        width=3)
    track_kb.row(
        InlineKeyboardButton(text="◀️", callback_data=Pagination(action="prev", page=page).pack()),
        InlineKeyboardButton(text="▶️", callback_data=Pagination(action="next", page=page).pack()),
        width=2

    )
    return track_kb.as_markup()


def paginator_tracks(page, list_tracks, id_album):
    list_title_tracks = [[track['title'], track['artist']] for track in list_tracks]
    count_tracks = len(list_title_tracks)

    count_last = count_tracks - page * 9

    track_kb = InlineKeyboardBuilder()
    if(count_tracks % 10 == 1 and count_tracks != 11 ):

        track_kb.row(
            InlineKeyboardButton(text=f"⬇️Скачать {count_last} трек",
                                 callback_data=PaginationTrackAlbum(action="down_all_tracks_t", page=page,count=count_tracks,
                                                                    id_album=id_album).pack()),
            InlineKeyboardButton(text="⬇️Скачать рандомный",
                                 callback_data=PaginationTrackAlbum(action="down_rand_t", page=page,count=count_tracks,
                                                                    id_album=id_album).pack()), width=2)
    elif(count_tracks % 10 <5):
        track_kb.row(
            InlineKeyboardButton(text=f"⬇️Скачать {count_last} трека",
                                 callback_data=PaginationTrackAlbum(action="down_all_tracks_t", page=page,
                                                                    count=count_tracks,
                                                                    id_album=id_album).pack()),
            InlineKeyboardButton(text="⬇️Скачать рандомный",
                                 callback_data=PaginationTrackAlbum(action="down_rand_t", page=page, count=count_tracks,
                                                                    id_album=id_album).pack()), width=2)
    else:
        track_kb.row(
            InlineKeyboardButton(text=f"⬇️Скачать {count_last} треков",
                                 callback_data=PaginationTrackAlbum(action="down_all_tracks_t", page=page,
                                                                    count=count_tracks,
                                                                    id_album=id_album).pack()),
            InlineKeyboardButton(text="⬇️Скачать рандомный",
                                 callback_data=PaginationTrackAlbum(action="down_rand_t", page=page, count=count_tracks,
                                                                    id_album=id_album).pack()), width=2)
    if(count_tracks>=3):
        for i in range(count_tracks // 3):

            track_kb.row(
                InlineKeyboardButton(text=f'{" - ".join(list_title_tracks[page * 9 + i * 3])}',
                                     callback_data=PaginationTrackAlbum(action=f'{1 + i * 3}-track_t',
                                                                        page=page,count=count_tracks, id_album=id_album).pack()),
                InlineKeyboardButton(text=f'{" - ".join(list_title_tracks[page * 9 + 1 + i * 3])}',
                                     callback_data=PaginationTrackAlbum(action=f'{2 + i * 3}-track_t',
                                                                        page=page, count=count_tracks, id_album=id_album).pack()),
                InlineKeyboardButton(text=f'{" - ".join(list_title_tracks[page * 9 + 2 + i * 3])}',
                                     callback_data=PaginationTrackAlbum(action=f'{3 + i * 3}-track_t',
                                                                        page=page,count=count_tracks, id_album=id_album).pack()),
                width=3)

    if(count_tracks >=2):
        for i in range(count_tracks % 3):

            track_kb.row(
                InlineKeyboardButton(text=f'{" - ".join(list_title_tracks[count_tracks - (2 - i) -1])}',
                                     callback_data=PaginationTrackAlbum(action=f'{1 + i * 3}-track_t',
                                                                        page=page,count=count_tracks, id_album=id_album).pack()),
                width=1)
        track_kb.row(
            InlineKeyboardButton(text=f'🔙Назад🔙',
                                 callback_data=PaginationTrackAlbum(action=f'back',
                                                                    page=page, count=count_tracks,
                                                                    id_album=id_album).pack()),
            width=1)
    if(count_tracks  == 1):
        track_kb.row(
            InlineKeyboardButton(text=f'{" - ".join(list_title_tracks[count_tracks - 1])}',
                                 callback_data=PaginationTrackAlbum(action=f'{1}-track_t',
                                                                    page=page, count=count_tracks,
                                                                    id_album=id_album).pack()),
            width=1)
        track_kb.row(
            InlineKeyboardButton(text=f'🔙Назад🔙',
                                 callback_data=PaginationTrackAlbum(action=f'back',
                                                                    page=page, count=count_tracks,
                                                                    id_album=id_album).pack()),
            width=1)
    return track_kb.as_markup()




def paginator_likes(page, list_favorite_tracks):
    if (len(list_favorite_tracks) != 0):

        track_kb = InlineKeyboardBuilder()
        track_kb.row(
            InlineKeyboardButton(text="⬇️Скачать 10 треков",
                                 callback_data=PaginationTrack(action="down_10_tracks_tr", page=page).pack()),
            InlineKeyboardButton(text="⬇️Скачать рандомный",
                                 callback_data=PaginationTrack(action="down_rand_tr", page=page).pack()),
            width=2
        )
        for i in range(3):
            track_kb.row(
                InlineKeyboardButton(text=f'{" - ".join(list_favorite_tracks[page * 10 + i * 3])}',
                                     callback_data=PaginationTrack(action=f'{1 + i * 3}-track_tr', page=page).pack()),
                InlineKeyboardButton(text=f'{" - ".join(list_favorite_tracks[page * 10 + 1 + i * 3])}',
                                     callback_data=PaginationTrack(action=f'{2 + i * 3}-track_tr', page=page).pack()),
                InlineKeyboardButton(text=f'{" - ".join(list_favorite_tracks[page * 10 + 2 + i * 3])}',
                                     callback_data=PaginationTrack(action=f'{3 + i * 3}-track_tr', page=page).pack()),

                width=3)
        track_kb.row(
            InlineKeyboardButton(text=f'{" - ".join(list_favorite_tracks[page * 10 + 9])}',
                                 callback_data=PaginationTrack(action=f'{10}-track_tr', page=page).pack()),
            width=1

        )
        track_kb.row(
            InlineKeyboardButton(text="◀️", callback_data=PaginationTrack(action="prev_t", page=page).pack()),
            InlineKeyboardButton(text="▶️", callback_data=PaginationTrack(action="next_t", page=page).pack()),
            width=2

        )
        return track_kb.as_markup()
    else:
        return "Ваш плейлист любимых треков пуст. Добавьте себе треки)..."


def paginator_albums(page, list_album):
    count_last = len(list_album) - page * 9
    track_kb = InlineKeyboardBuilder()
    if(count_last >= 9):

        for i in range(3):
            track_kb.row(
                InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + i * 3])}',
                                     callback_data=PaginationAlbum(action=f'{1 + i * 3}_a', page=page).pack()),
                InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + 1 + i * 3])}',
                                     callback_data=PaginationAlbum(action=f'{2 + i * 3}_a', page=page).pack()),
                InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + 2 + i * 3])}',
                                     callback_data=PaginationAlbum(action=f'{3 + i * 3}_a', page=page).pack()),
                width=3)
    if(count_last < 9):
        if(count_last% 3 == 0):
            for i in range((len(list_album)- page*9)//3):
                track_kb.row(
                    InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + i * 3])}',
                                         callback_data=PaginationAlbum(action=f'{1 + i * 3}_a', page=page).pack()),
                    InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + 1 + i * 3])}',
                                         callback_data=PaginationAlbum(action=f'{2 + i * 3}_a', page=page).pack()),
                    InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + 2 + i * 3])}',
                                         callback_data=PaginationAlbum(action=f'{3 + i * 3}_a', page=page).pack()),
                    width=3)
        else:
            for i in range((len(list_album)- page*9)):
                track_kb.row(
                    InlineKeyboardButton(text=f'{" - ".join(list_album[page * 9 + i])}',
                                         callback_data=PaginationAlbum(action=f'{1 + i * 3}_a', page=page).pack()),
                    width=1)
    track_kb.row(
        InlineKeyboardButton(text="◀️", callback_data=PaginationAlbum(action="prev_a", page=page).pack()),
        InlineKeyboardButton(text="▶️", callback_data=PaginationAlbum(action="next_a", page=page).pack()),
        width=2

    )
    return track_kb.as_markup()


def action_user():
    action = InlineKeyboardBuilder()
    action.row(InlineKeyboardButton(text="Расширение Chrome",
                                    url='https://chrome.google.com/webstore/detail/yandex-music-token/lcbjeookjibfhjjopieifgjnhlegmkib'),
               InlineKeyboardButton(text="Авторизация через Яндекс",
                                 url='https://oauth.yandex.ru/authorize?response_type=token&client_id=30075430e32543be905c1d7c76a5515d'),
               InlineKeyboardButton(text="Приложение для Андроид", url='https://disk.yandex.ru/d/aFUXDggXveGaWg'))
    action.row(InlineKeyboardButton(text="❌Не хочу вводить токен", callback_data=Action(action="no_action").pack()),
               width=1)
    return action.as_markup()


def user_info():
    profile = InlineKeyboardBuilder()
    profile.row(InlineKeyboardButton(text="Заполнить данные о себе", callback_data=Action(action="profile").pack()),
                width=1)
    return profile.as_markup()
