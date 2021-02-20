#!/usr/bin/env python3.5
################################################################################### config
HODOR = ["Hodor!", "Я есть грут!", "Хуедор!", "Да отстань ты!", "Ходор!", "Ходор, ходор!", " Hold The Door!", "🤬","😡","🤯","🤮" ]
TOKEN_HODOR = '' #token
################################################################################### library
import telebot
import time
import bs4
import requests
from random import randrange
from telebot import types
from telebot import apihelper
#If you want to use socket5 proxy you need install dependency pip install requests[socks] 
# and make sure, that you have the latest version of gunicorn, PySocks, pyTelegramBotAPI, 
# requests and urllib3.
################################################################################### proxy
def proxy():
    proxy_fin=[]
    while True:
        try:
            proxy=requests.get('https://www.us-proxy.org/')
            if proxy.ok==True:
                proxy_html=bs4.BeautifulSoup(proxy.text, "html.parser")
                for f in range(100):
                    proxy_fin.append(proxy_html.tbody('td')[f*8].text+':'+proxy_html.tbody('td')[f*8+1].text)
                break
        except Exception:
            time.sleep(10)
    return proxy_fin
proxy_fin=proxy()
apihelper.CONNECT_TIMEOUT = 15
ii=0 # прокси
while ii<len(proxy_fin):
    apihelper.proxy = {
        'http': 'http://'+proxy_fin[ii],
        'https': 'https://'+proxy_fin[ii]
    }
    bot = telebot.TeleBot(TOKEN_HODOR, threaded=False)
    try:
        bot.get_me()
        #bot.send_message('', proxy_fin[ii]) # user id можно вставить
        break
    except Exception:
        ii+=1
        time.sleep(4)
        if ii == len(proxy_fin)-1:
            ii=0
            proxy_fin=proxy()
################################################################################### keyboard
markup = types.ReplyKeyboardMarkup(True)
markup.row('/hodor')
################################################################################### hodor
@bot.message_handler(commands=['start','hodor'])
def handle_hodor(message):
    answer = HODOR[randrange(len(HODOR))]
    bot.send_message(message.chat.id, answer, reply_markup=markup)
################################################################################### main
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=20)
        except Exception:
            time.sleep(3)
            proxy_fin=proxy()
            apihelper.CONNECT_TIMEOUT = 15
            ii=0
            while ii<len(proxy_fin):
                apihelper.proxy = {
                    'http': 'http://'+proxy_fin[ii],
                    'https': 'https://'+proxy_fin[ii]
                }
                try:
                    bot.get_me()
                    #bot.send_message('', proxy_fin[ii]) # user id можно вставить
                    break
                except Exception:
                    time.sleep(1)
                    ii+=1
                    if ii==len(proxy_fin)-1:
                        ii=0
                        proxy_fin=proxy()
