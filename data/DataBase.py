import time
import requests
import psycopg2
from psycopg2 import sql

from peewee import *
from peewee import _atomic, IntegrityError

db = PostgresqlDatabase(database='YandexMusic', user='postgres', password='123', host='localhost', port='5432')
# Подключение к базе данных
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class users(BaseModel):
    user_id = PrimaryKeyField()
    username = CharField()
    token = CharField()
    role = IntegerField()  # 1 or 2 or 3 (adm , vip, default)
    bitrate = IntegerField(null=False)


class albums(BaseModel):
    album_id = PrimaryKeyField()
    yandex_music_id = CharField()
    title = CharField()
    artist = CharField()


class tracks(BaseModel):
    track_id = PrimaryKeyField()
    yandex_music_id = CharField()
    title = CharField()
    artist = CharField()
    album_id = ForeignKeyField(albums, backref='tracks')
    date_added = DateTimeField()


class chart(BaseModel):
    track_id = PrimaryKeyField()
    title_track = CharField()
    album_id = ForeignKeyField(albums, backref='chart')
    title_album = CharField()
    artist = CharField()
    position = IntegerField(unique=True)


class usertracks(BaseModel):
    user_id = ForeignKeyField(users, backref='usertracks')
    track_id = ForeignKeyField(tracks, backref='usertracks')
    date_added = DateTimeField()


class albumtracks(BaseModel):
    album_id = ForeignKeyField(albums, backref='albumtracks')
    track_id = ForeignKeyField(tracks, backref='albumtracks')


class playlists(BaseModel):
    playlist_id = PrimaryKeyField()
    user_id = ForeignKeyField(users, backref='playlists')
    title = CharField()


class playlisttracks(BaseModel):
    playlist_id = ForeignKeyField(playlists, backref='playlisttracks')
    track_id = ForeignKeyField(tracks, backref='playlisttracks')
    date_added = DateTimeField()


with db:
    db.create_tables([users, albums, tracks, albumtracks, playlists, playlisttracks])


def is_user(user_id):
    query = users.select().where(users.user_id == user_id)
    record_exists = query.exists()
    if (record_exists == True):
        return 1
    else:
        return 0


def get_token(user_id):
    user_token = users.select(users.token).where(users.user_id == f"{user_id}").alias('user_token')
    result = []
    for row in user_token.execute():
        result.append({
            'token': row.token
        })
    print(result[0]["token"])
    return result[0]['token']


def insert_tracks_users_favorite(user_login):
    response, counttracks = response_likes_tracks(user_login)
    if (response.status_code == 200):

        for i in range(0, counttracks):
            id_track = response.json()[i]['id']
            id_album = response.json()[i]['albums'][0]['id']
            artist = response.json()[i]['albums'][0]['artists']
            title = response.json()[i]['title']
            album_title = response.json()[i]['albums'][0]['title']

            autors = ', '.join([artist['name'] for artist in artist])
            # list_tracks.append([track__id, album_id, title, artists])
            result = insert_track_with_album(id_track, id_album, title, album_title, autors)
            print(result)


def insert_usertracks(user_id, user_login):
    response, counttracks = response_likes_tracks(user_login)
    if (response.status_code == 200):

        for i in range(0, counttracks):
            id_track = response.json()[i]['id']

            result = insert_track_user(user_id, id_track)
            print(result)


def insert_track_chart(track_id, title_track, album_id, title_album, artist, position):
    try:

        # Вставка трека с обработкой конфликта
        pkey1 = chart.insert(
            track_id=track_id,
            title_track=title_track,
            album_id=album_id,
            title_album=title_album,
            artist=artist,
            position=position

        ).execute()

        return pkey1 if pkey1 else 0
    except IntegrityError:
        return f'Ошибка с треком {track_id, title_track, position}'


def update_chart_list():
    params_chart = {
        'what': 'chart',
        'lang': 'ru',
        'external-domain': 'music.yandex.ru',
        'overembed': 'false',
        'ncrnd': '0.0002524140258985952',
    }
    headers_chart = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://music.yandex.ru/chart',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',

        'X-KL-kfa-Ajax-Request': 'Ajax_Request',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Retpath-Y': 'https://music.yandex.ru/chart',
        'X-Yandex-Music-Client-Now': '2023-12-09T18:33:17+03:00',
        'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params_chart, headers=headers_chart)
    print(response.status_code)
    # pprint(response.json()['chartPositions'])
    if (response.status_code == 200):

        chart.delete().execute()

        for track in response.json()['chartPositions']:
            position = track['chartPosition']['position']
            title = track['track']['title']
            artists = [artist['name'] for artist in track['track']['artists']]
            album_title = track['track']['albums'][0]['title']
            autors = ', '.join(artists)
            id_track = track['track']['id']
            id_album = track['track']['albums'][0]['id']

            print(insert_track_chart(id_track, title, id_album, album_title, autors, position))
        return 'Чарт обновлен'
    return 1


def get_list_select_user_favorite_tracks(user_id):

    query = (
        tracks
        .select(tracks.yandex_music_id, tracks.title, tracks.artist)
        .join(usertracks, on=(usertracks.track_id == tracks.yandex_music_id))
        .where(usertracks.user_id == user_id))



    list_tracks_info = []
    for row in query:

        list_tracks_info.append({
            'track_id': row.yandex_music_id,
            'title':  row.title,
            'artist': row.artist
        })
    # print(list_tracks_info)
    return list_tracks_info

        # print(row.track_id, tracks.title, tracks.artist)



def update_favorite_tracks(user_id):
    login = get_user_login(user_id)
    response, counttracks = response_likes_tracks(login)
    if response.status_code == 200:
        i = 0
        flag = 1
        while(i < counttracks and flag != 0):
            id_track = response.json()[i]['id']
            id_album = response.json()[i]['albums'][0]['id']
            artist = response.json()[i]['albums'][0]['artists']
            title = response.json()[i]['title']
            album_title = response.json()[i]['albums'][0]['title']
            autors = ', '.join([artist['name'] for artist in artist])
            if(check_track(id_track)==1):
                flag = 0
            result = insert_track_with_album(id_track, id_album, title, album_title, autors)
            result2 = insert_track_user(user_id, id_track)
            i += 1
            print(result, result2)

    # list_tracks = []
    # track = usertracks.select(usertracks.user_id, usertracks.track_id, usertracks.date_added).where(
    #     usertracks.user_id == user_id)
    # for row in track.execute():
    #     list_tracks.append({
    #         'user_id': row.user_id,
    #         'track_id': row.track_id,
    #         'date_added': row.date_added
    #     })
    # return list_tracks


def insert_track_with_album(id_track, id_album, title_track, title_album, artists):
    try:
        with db.atomic():
            # Вставка трека с обработкой конфликта
            pkey1 = tracks.insert(
                yandex_music_id=id_track,
                title=title_track,
                artist=artists,
                album_id=id_album
            ).on_conflict('IGNORE').execute()

            # Вставка альбома с обработкой конфликта
            pkey2 = albums.insert(
                yandex_music_id=id_album,
                title=title_album,
                artist=artists
            ).on_conflict('IGNORE').execute()

            return pkey1, pkey2 if pkey1 and pkey2 else pkey1 if pkey1 else 0
    except IntegrityError:
        return 0


# print(insert_track_with_album( 52950078, 9168267, 'Paint It Black', 'Paint It Black Remixes',' Danny Darko, Julien Kelland'))

def insert_track_user(user__id, track__id):
    try:
        with db.atomic():
            # Вставка track_id с обработкой конфликта
            date_added = tracks.select(tracks.date_added).where(tracks.yandex_music_id == track__id).scalar()
            print(date_added)
            pkey = usertracks.insert(
                user_id=user__id,
                track_id=track__id,
                date_added=date_added

            ).on_conflict('IGNORE').execute()
            return pkey if pkey else 0
    except IntegrityError:
        return 0


def add_user(tg_id, login, token, role, bitrate):
    query = users.select().where(users.user_id == tg_id)

    record_exists = query.exists()
    if record_exists == False:
        user_info = users.insert(user_id=tg_id, username=login, token=token, role=role, bitrate=bitrate)
        user_info.execute()


def check_track(id_track):
    query = tracks.select().where(tracks.yandex_music_id == id_track)
    record_exists = query.exists()
    if record_exists == False:
        return 0
    else:
        return 1

# print(add_user(794845497, 'minko.serezha2022', 'AQAAAAArbx-eAAG8Xq5LWimUC0qykmWaf2wSXqk', 2, 192))

def get_list_chart_tracks():
    list_tracks = []

    # Вставка track_id с обработкой конфликта
    track = chart.select(chart.title_track, chart.artist, chart.track_id)
    for row in track.execute():
        list_tracks.append({
            'title': row.title_track,
            'artist': row.artist,
            'track_id': row.track_id
        })
    return list_tracks


list_chart_tracks_tuple = get_list_chart_tracks()

list_title_tracks_chart = [[track['title'], track['artist']] for track in list_chart_tracks_tuple]


def get_users_info():
    user = (users.select(users.user_id, users.username, users.token, users.role)).alias('users')
    result = []
    for row in user.execute():
        result.append({
            'ID': row.user_id,
            'Login': row.username,
            'Token': row.token,
            'Role': row.role
        })
    return result


def get_user_role(user_id):
    user_role = users.select(users.role).where(users.user_id == f"{user_id}").alias('user_role')
    result = []
    for row in user_role.execute():
        result.append({
            'Role': row.role
        })
    return result[0]["Role"]


def get_user_id(login):
    user_id = users.select(users.user_id).where(users.username == f"{login}").alias('user_id')
    result = []
    for row in user_id.execute():
        result.append({
            'Id': row.user_id
        })
    return result[0]["Id"]


def get_user_login(user_id):
    user_login = users.select(users.username).where(users.user_id == f"{user_id}").alias('user_login')
    result = []
    for row in user_login.execute():
        result.append({
            'Login': row.username
        })
    return result[0]["Login"]


def get_user_role_with_login(login):
    user_role = users.select(users.role).where(users.username == f"{login}").alias('user_role')
    result = []
    for row in user_role.execute():
        result.append({
            'Role': row.role
        })
    return result[0]["Role"]


def get_logins():
    logins = users.select(users.username).alias('logins')
    result = []
    for row in logins.execute():
        result.append({
            'Login': row.username
        })
    return [result[i]['Login'] for i in range(len(result))]


# def get_tracks_name_user(user_id):
#
login_user = get_logins()


# запрос на количество лайкнутых треков
def response_likes_tracks(login):
    headers1 = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': f'https://music.yandex.ru/users/{login}/tracks',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',

        'X-KL-kfa-Ajax-Request': 'Ajax_Request',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Retpath-Y': f'https://music.yandex.ru/users/{login}/tracks',
        'X-Yandex-Music-Client-Now': '2023-12-09T23:04:43+03:00',
        'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params_favorite_tracks = {
        'owner': f'{login}',
        'filter': 'tracks',
        'likeFilter': 'favorite',
        'kidsSubPage': '',
        'page': '0',
        'sort': '',
        'dir': '',
        'lang': 'ru',
        'external-domain': 'music.yandex.ru',
        'overembed': 'false',
        'ncrnd': '0.9414629080521095',
    }

    response_tracks_id = requests.get('https://music.yandex.ru/handlers/library.jsx', params=params_favorite_tracks,
                                      headers=headers1)
    # pprint(response.json())
    listracks_id = ','.join(response_tracks_id.json()['trackIds'])
    # print(listracks_id)
    counttracks = len(response_tracks_id.json()['trackIds'])

    headers2 = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://music.yandex.ru',
        'Referer': f'https://music.yandex.ru/users/{login}/tracks',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
        'X-Current-UID': '563351686',
        'X-KL-kfa-Ajax-Request': 'Ajax_Request',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Retpath-Y': f'https://music.yandex.ru/users/{login}/tracks',
        'X-Yandex-Music-Client-Now': '2023-12-12T02:35:38+03:00',
        'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'entries': listracks_id,
        'strict': 'true',
        'removeDuplicates': 'false',
        'lang': 'ru',
        'sign': 'a21db53fbe51d3192dd86cbf99aee63016624cf2:1702337736810',
        'external-domain': 'music.yandex.ru',
        'overembed': 'false',
    }

    response = requests.post('https://music.yandex.ru/handlers/track-entries.jsx', headers=headers2, data=data)
    return response, counttracks
