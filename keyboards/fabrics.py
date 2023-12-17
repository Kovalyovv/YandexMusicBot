from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from data import DataBase
from typing import Union

class Pagination(CallbackData, prefix="pag"):
    action: str
    page: int


class PaginationTrack(CallbackData, prefix="pag_tr"):
    action: str
    list_title_tracks_likes: list
    page: int


class Action(CallbackData, prefix="act"):
    action: str


list_title_tracks_chart = DataBase.list_title_tracks_chart


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









def paginator_likes(page: int = 0, list_title_tracks_likes: list = []):

    track_kb = InlineKeyboardBuilder()
    track_kb.row(
        InlineKeyboardButton(text="⬇️Скачать 10 треков",
                             callback_data=PaginationTrack(action="down_10_tracks_tr", page=page).pack()),
        InlineKeyboardButton(text="⬇️Скачать рандомный",
                             callback_data=PaginationTrack(action="down_rand_tr", page=page).pack()),
        width=2
    )
    track_kb.row(
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10])}',
                             callback_data=PaginationTrack(action='1-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 1])}',
                             callback_data=PaginationTrack(action='2-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 2])}',
                             callback_data=PaginationTrack(action='3-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 3])}',
                             callback_data=PaginationTrack(action='4-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 4])}',
                             callback_data=PaginationTrack(action='5-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 5])}',
                             callback_data=PaginationTrack(action='6-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 6])}',
                             callback_data=PaginationTrack(action='7-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 7])}',
                             callback_data=PaginationTrack(action='8-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 8])}',
                             callback_data=PaginationTrack(action='9-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text=f'{" - ".join(list_title_tracks_likes[page * 10 + 9])}',
                             callback_data=PaginationTrack(action='10-track_tr', list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        width=3)
    track_kb.row(
        InlineKeyboardButton(text="◀️", callback_data=PaginationTrack(action="prev_tr", list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        InlineKeyboardButton(text="▶️", callback_data=PaginationTrack(action="next_tr", list_title_tracks_likes = list_title_tracks_likes, page=page).pack()),
        width=2

    )
    return track_kb.as_markup()




def action_user():
    action = InlineKeyboardBuilder()
    action.row(InlineKeyboardButton(text="❌Не хочу вводить токен", callback_data=Action(action="no_action").pack()),
               width=1)
    return action.as_markup()


def user_info():
    profile = InlineKeyboardBuilder()
    profile.row(InlineKeyboardButton(text="Заполнить данные о себе", callback_data=Action(action="profile").pack()), width=1)
    return profile.as_markup()
