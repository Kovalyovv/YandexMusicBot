# import DataBase
from yandex_music import Client

from data import DataBase

client = Client('y0_AgAAAAAhlBCGAAG8XgAAAAD0UyzdQynAQ65FSKa0gSsmLfAzmVZDyd0').init()
# https://music.yandex.ru/#access_token=&token_type=bearer&expires_in=31398203
# https://music.yandex.ru/#access_token=y0_AgAAAAAnyT1KAAG8XgAAAAD0YStXsI7S46mITHuPzAPHHt2r9CiDQHI&token_type=bearer&expires_in=31536000

# track = client.tracks(['40597465', '118465150'])[1]
# track.download(f"Сер.mp3", 'mp3', 320)


# response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=responses.params_chart, headers=responses.headers_chart)
# print(response.status_code)
# # pprint(response.json()['chartPositions'])
# for track in response.json()['chartPositions']:
#     position = track['chartPosition']['position']
#     title = track['track']['title']
#
#     artists = [artist['name'] for artist in track['track']['artists']]
#
#     album_title =  track['track']['albums'][0]['title']
#     autors = ', '.join(artists)
#     id_track = track['track']['id']
#     id_album = track['track']['albums'][0]['id']

    # print(DataBase.call_my_function(int(id_track), int(id_album), title, album_title, autors))
    # Пример использования функции


    # print(f"№ {position}  {title} - {autors} ({id_track} {id_album})")


# login_user = DataBase.get_logins()
#
# headers_chart = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'ru,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Referer': 'https://music.yandex.ru/chart',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
#
#     'X-KL-kfa-Ajax-Request': 'Ajax_Request',
#     'X-Requested-With': 'XMLHttpRequest',
#     'X-Retpath-Y': 'https://music.yandex.ru/chart',
#     'X-Yandex-Music-Client-Now': '2023-12-09T18:33:17+03:00',
#     'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# params_chart = {
#     'what': 'chart',
#     'lang': 'ru',
#     'external-domain': 'music.yandex.ru',
#     'overembed': 'false',
#     'ncrnd': '0.0002524140258985952',
# }
#
#
#
# # запрос на количество лайкнутых треков
# headers1 = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'ru,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Referer': f'https://music.yandex.ru/users/{login_user[0]}/tracks',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
#
#     'X-KL-kfa-Ajax-Request': 'Ajax_Request',
#     'X-Requested-With': 'XMLHttpRequest',
#     'X-Retpath-Y': 'https://music.yandex.ru/users/dmitriykovalyov2003/tracks',
#     'X-Yandex-Music-Client-Now': '2023-12-09T23:04:43+03:00',
#     'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# params_favorite_tracks = {
#     'owner': f'{login_user[0]}',
#     'filter': 'tracks',
#     'likeFilter': 'favorite',
#     'kidsSubPage': '',
#     'page': '0',
#     'sort': '',
#     'dir': '',
#     'lang': 'ru',
#     'external-domain': 'music.yandex.ru',
#     'overembed': 'false',
#     'ncrnd': '0.9414629080521095',
# }
#
#
# response_tracks_id = requests.get('https://music.yandex.ru/handlers/library.jsx', params=params_favorite_tracks, headers=headers1)
# # pprint(response.json())
# listracks_id = ','.join(response_tracks_id.json()['trackIds'])
# # print(listracks_id)
# counttracks = len(response_tracks_id.json()['trackIds'])
#
#
#
#
#
#
# # track_short.track = Track(client.users_likes_tracks()[3].track())
# # title_track = client.users_likes_tracks()[2].fetch_track().title.replace('?', '').replace('|','').replace('/','').replace('\\','').replace('"','').replace(':','').replace('*','')
# # track_artist = client.users_likes_tracks()[2].fetch_track()['artists'][1]['name']
# # artists = ','.join([artist['name'] for artist in client.users_likes_tracks()[2].fetch_track()['artists']])
# #
# # # client.users_likes_tracks()[2].fetch_track().download(f"{title_track}_{track_artist}.mp3", 'mp3', 320)
# # track = client.tracks(['40597465'])[0]
# # track.download(f"Сер.mp3", 'mp3', 320)
# # pprint(track)
# headers2 = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'ru,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     'Origin': 'https://music.yandex.ru',
#     'Referer': f'https://music.yandex.ru/users/{login_user[0]}/tracks',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.731 YaBrowser/23.11.1.731 Yowser/2.5 Safari/537.36',
#     'X-Current-UID': '563351686',
#     'X-KL-kfa-Ajax-Request': 'Ajax_Request',
#     'X-Requested-With': 'XMLHttpRequest',
#     'X-Retpath-Y': f'https://music.yandex.ru/users/{login_user[0]}/tracks',
#     'X-Yandex-Music-Client-Now': '2023-12-12T02:35:38+03:00',
#     'sec-ch-ua': '"Chromium";v="118", "YaBrowser";v="23", "Not=A?Brand";v="99"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# data = {
#     'entries': listracks_id,
#     'strict': 'true',
#     'removeDuplicates': 'false',
#     'lang': 'ru',
#     'sign': 'a21db53fbe51d3192dd86cbf99aee63016624cf2:1702337736810',
#     'external-domain': 'music.yandex.ru',
#     'overembed': 'false',
# }
#
#
# response = requests.post('https://music.yandex.ru/handlers/track-entries.jsx', headers=headers2, data=data)
# pprint(response.json())
# pprint(response.status_code)
# pprint(response.json()[0]['albums'][0]['artists'])
# list_tracks = []

# print(insert_tracks_users_favorite(response))
    # print(list_tracks[i][2], list_tracks[i][3])
# print(insert_tracks_users_favorite(response))
   # print( f'{track.title}{artists}')


# client.users_likes_tracks()[3].fetch_track().download(f"{track.title}_{track.artists}.mp3", 'mp3', 320)

# result = DataBase.insert_track_with_album(id_track, id_album, title, album_title, autors)
#     print(result)