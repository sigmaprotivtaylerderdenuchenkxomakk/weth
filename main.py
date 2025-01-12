from requests import *
from telebot import types
import telebot
TOKEN = "7345251836:AAFyEw6TwmMl5YS0yWBtnYzenB4zu3llT3I"
bot = telebot.TeleBot(TOKEN)
def weth(cn,b=5):
    res = get(
        url = 'https://api.openweathermap.org/data/2.5/forecast',
        params={
            'appid':'1e29b1de4251866ff15108fd103bd241',
            'q': cn,
            'cnt': b,
            'lang':'ru',
            'units':'metric'
            }
        )


    return res

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Отправте название города')
    bot.register_next_step_handler(message, input_use_name)

@bot.message_handler(content_types=['text'])
def handle_start1(message):
    bot.send_message(message.chat.id, 'введите /start')


def input_use_name(message: types.Message):
    user_name = message.text.strip()
    k = telebot.types.InlineKeyboardMarkup()
    for i in range(1,6):
        j = telebot.types.InlineKeyboardButton(f'{9+i*3} часов', callback_data=f'{i} '+user_name)
        k.add(j)
    bot.send_message(chat_id = message.chat.id, text= 'Выберите до какого часа: ',reply_markup=k)
    # if len(user_name)!=2:
    #     res = weth(user_name[0])
    # else:
    #      res = weth(user_name[0],user_name[1])
    # if res.status_code == 200:
    #     data = res.json()
    #     for day in data.get('list'):
    #             tmp = day.get('main').get('temp')
    #             des = day.get('weather')[0].get('description')
    #             w = day.get("main").get("humidity")
    #             bot.send_message(message.chat.id, f'{day.get('dt_txt')}: {tmp},{des}, влажность: {w}%')
    # else:
    #      bot.send_message(message.chat.id, "ЛЯ ты не чил гай")
    #      bot.send_message(message.chat.id, 'Отправте название города и через пробел на сколько часов вперед(можно не вводить)')
    #      bot.register_next_step_handler(message, input_use_name)


@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    bot.delete_message(callback.message.chat.id, callback.message.message_id)
    res = weth(callback.data.split()[1],callback.data.split()[0])
    if res.status_code == 200:
        data = res.json()
        for day in data.get('list'):
                tmp = day.get('main').get('temp')
                des = day.get('weather')[0].get('description')
                w = day.get("main").get("humidity")
                bot.send_message(callback.message.chat.id, f'{day.get('dt_txt')}: {tmp},{des}, влажность: {w}%')
        bot.send_message(callback.message.chat.id, 'введите /start')
    else:
         bot.send_message(callback.message.chat.id, "ЛЯ ты не чил гай")
         bot.send_message(callback.message.chat.id, 'Отправте название города')
         bot.register_next_step_handler(callback.message, input_use_name)
bot.polling(non_stop=True, interval=1)
