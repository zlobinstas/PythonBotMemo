import telebot 
import webbrowser
from telebot import types

#Buttom with link:
def add_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Sponsor this project', 'https://github.com/zlobinstas'))
    return markup
#for using it: use reply_markup at the methods reply_to or send_message

bot = telebot.TeleBot('5501926269:AAFrN3-JX-kdYa5q4AYcEKg_5QIV4nNgZlc')

@bot.message_handler(commands=['site', 'website'])
def site(message):
     webbrowser.open('https://github.com/zlobinstas')

@bot.message_handler(commands=['start'])
def welcome(message):
     bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name} {message.from_user.last_name}!\nPlease, write me your notification in format:\n 'DD-MM-YY = My notification'\n\nFor example: 03-02-2022 = Create new Telegram Bot", reply_markup=add_markup()) 

bot.polling(non_stop=True) 