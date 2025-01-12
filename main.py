from requests import *
import telebot.types
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
    k = telebot.types.InlineKeyboardMarkup()
    
    j = telebot.types.InlineKeyboardButton('да', callback_data='0')

    l = telebot.types.InlineKeyboardButton('нет', callback_data='1')
    
    k.add(j)
    k.add(l)
    k.add(gh)
    bot.send_message(message.chat.id, 'Отправте название города и через пробел на сколько часов вперед(можно не вводить)',reply_markup=k)
    bot.register_next_step_handler(message, input_use_name)

@bot.message_handler(content_types=['text'])
def handle_start1(message):
    bot.send_message(message.chat.id, 'введите /start')


def input_use_name(message):
    user_name = message.text.strip().split()
    if len(user_name)!=2:
        res = weth(user_name[0])
    else:
         res = weth(user_name[0],user_name[1])
    if res.status_code == 200:
        data = res.json()
        for day in data.get('list'):
                tmp = day.get('main').get('temp')
                des = day.get('weather')[0].get('description')
                w = day.get("main").get("humidity")
                bot.send_message(message.chat.id, f'{day.get('dt_txt')}: {tmp},{des}, влажность: {w}%')
    else:
         bot.send_message(message.chat.id, "ЛЯ ты не чил гай")
         bot.send_message(message.chat.id, 'Отправте название города и через пробел на сколько часов вперед(можно не вводить)')
         bot.register_next_step_handler(message, input_use_name)

bot.polling(non_stop=True, interval=1)
