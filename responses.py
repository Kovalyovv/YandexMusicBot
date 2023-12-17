
import requests
from data import DataBase
from yandex_music import ClientAsync

client = ClientAsync('y0_AgAAAAAhlBCGAAG8XgAAAAD0UyzdQynAQ65FSKa0gSsmLfAzmVZDyd0').init()


# y0_AgAAAAAWnOL8AAG8XgAAAAD0W4H_QsZGsAzlQkOFxfjle_UBOIz4WcE
# https://music.yandex.ru/#access_token=y0_AgAAAAAnyT1KAAG8XgAAAAD0YStXsI7S46mITHuPzAPHHt2r9CiDQHI&token_type=bearer&expires_in=31536000

def check_token(token):
    import requests
    headers = {
        'Accept': 'application/json; q=1.0, text/*; q=0.8, */*; q=0.1',
        'Accept-Language': 'ru,en;q=0.9',
        'Connection': 'keep-alive',
        'Referer': 'https://music.yandex.ru/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
        'X-KL-kfa-Ajax-Request': 'Ajax_Request',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Retpath-Y': f'https%3A%2F%2Fmusic.yandex.ru%2F%23access_token%3D{token}26token_type%3Dbearer%26expires_in%3D30897175',
        'X-Yandex-Music-Client': 'YandexMusicAPI',
        'X-Yandex-Music-Client-Now': '2023-12-17T21:40:52+03:00',
        'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'external-domain': 'music.yandex.ru',
        'overembed': 'no',
        '__t': '1702838452373',
    }

    response = requests.get('https://music.yandex.ru/api/v2.1/handlers/auth', params=params, headers=headers)
    if response.status_code == 200:
        print(response.status_code)
        return 1
    else:
        return 0





# print(DataBase.call_my_function(int(id_track), int(id_album), title, album_title, autors))
# Пример использования функции
# print(f"№ {position}  {title} - {autors} ({id_track} {id_album})")




# track_short.track = Track(client.users_likes_tracks()[3].track())
# title_track = client.users_likes_tracks()[2].fetch_track().title.replace('?', '').replace('|','').replace('/','').replace('\\','').replace('"','').replace(':','').replace('*','')
# track_artist = client.users_likes_tracks()[2].fetch_track()['artists'][1]['name']
# artists = ','.join([artist['name'] for artist in client.users_likes_tracks()[2].fetch_track()['artists']])
#
# # client.users_likes_tracks()[2].fetch_track().download(f"{title_track}_{track_artist}.mp3", 'mp3', 320)
# track = client.tracks(['40597465'])[0]
# track.download(f"Сер.mp3", 'mp3', 320)
# pprint(track)


# pprint(response.json())
# pprint(response.status_code)
# pprint(response.json()[0]['albums'][0]['artists'])
# list_tracks = []


# запрос по трекам(название и исполнитель)

# без авторизации недоступен список треков альбома

# ALBUM_ID = 28498420
#
#
# album = client.albums_with_tracks(ALBUM_ID)
# tracks = []
# for i, volume in enumerate(album.volumes):
#     if len(album.volumes) > 1:
#         tracks.append(f'💿 Диск {i + 1}')
#     tracks += volume
#
# text = 'АЛЬБОМ\n\n'
# text += f'{album.title}\n'
# text += f"Исполнитель: {', '.join([artist.name for artist in album.artists])}\n"
# text += f'{album.year} · {album.genre}\n'
#
# cover = album.cover_uri
# if cover:
#     text += f'Обложка: {cover.replace("%%", "400x400")}\n\n'
#
# text += 'Список треков:'
#
# print(text)
#
# for track in tracks:
#     if isinstance(track, str):
#         print(track)
#     else:
#         artists = ''
#         if track.artists:
#             artists = ' - ' + ', '.join(artist.name for artist in track.artists)
#         print(track.title + artists)
