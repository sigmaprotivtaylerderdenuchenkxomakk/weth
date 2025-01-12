from requests import *
from pprint import pprint

def get_movie_info_omdb(cn):
    res = get(
        url = 'https://api.openweathermap.org/data/2.5/weather',
        params={
            'appid':'1e29b1de4251866ff15108fd103bd241',
            'q': cn,
            'lang':'ru',
            'units':'metric'
            }
    )


    if res.status_code == 200:
        data = res.json()
        print(data)
        print(f'Текущая температура в городе {cn}: {data.get('main').get('temp')} , {data.get('weather')[0].get('description')}, влажность: {data.get('main').get('humidity')}%')
        
    else:
        print('no, error code ========== 404')



get_movie_info_omdb('новосибирск')