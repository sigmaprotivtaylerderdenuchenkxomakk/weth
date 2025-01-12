from requests import *
import telebot
TOKEN = "7345251836:AAFyEw6TwmMl5YS0yWBtnYzenB4zu3llT3I"

bot = telebot.TeleBot(TOKEN)

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
        return f'Текущая температура в городе {cn}: {data.get('main').get('temp')} , {data.get('weather')[0].get('description')}, влажность: {data.get('main').get('humidity')}%'
        
    else:
        print('no, error code ========== 404')
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Отправте название города')
    bot.register_next_step_handler(message, input_use_name)

def input_use_name(message):
    user_name = message.text.strip()
    bot.send_message(message.chat.id, get_movie_info_omdb(user_name))
bot.polling(non_stop=True, interval=1)