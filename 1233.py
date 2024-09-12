import sqlite3

import telebot
from telebot import types
from postgres_client import save_phone_to_db
# import sqllite_client
# pip install pyTelegramBotAPI
# https://t.me/lesson1_1223_bot





bot = telebot.TeleBot("7304078340:AAHk9Ojoe0EI2gC37ylPFUTIkcDPRbTzwvg", parse_mode='HTML')
@bot.message_handler(commands=['start'])
def run2(message):
    keyboard = types.ReplyKeyboardMarkup()
    button_phone = types.KeyboardButton(text="Отправить номер", request_contact=True)
    keyboard.add(button_phone)
    bot.send_message(message.chat.id, 'Спасибо, ok с вами свяжемся', reply_markup=keyboard)

