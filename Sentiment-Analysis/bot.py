# -*- coding: utf-8 -*-
import os
import time

import config
import telebot
from telebot import types
import os
import time
import random
from SQLighter import SQLighter

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['test'])
def find_file_ids(message):
    for file in os.listdir('music/'):
        if file.split('.')[-1] == 'ogg':
            f = open('music/' + file, 'rb')
            res = bot.send_voice(message.chat.id, f, None)
            print(res)
        time.sleep(3)


@bot.message_handler(commands=['Choose'])
def choose_god(message):
    markup = types.ReplyKeyboardMarkup()
    markup.row('J', 'A')
    bot.send_message(message.chat.id, reply_markup=markup)


@bot.message_handler(content_types=["text"])  
def echo_messages(message):
    if message.text == 'blindWidow':
        bot.send_message(message.chat.id, '')
        bot.send_photo(message.chat.id, 'AgADAgAD5KcxG1oTFAcL8_Fua6HkmzQJSw0ABP5exCrEOlWRyksAAgI')
    elif message.text == 'A':
        bot.send_message(message.chat.id, '')
    elif message.text == 'J':
        bot.send_message(message.chat.id,
                         '')
    else:
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
