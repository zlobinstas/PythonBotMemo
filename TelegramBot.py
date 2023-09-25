import telebot 
import webbrowser
from telebot import types
import sqlite3

bot = telebot.TeleBot('5501926269:AAFrN3-JX-kdYa5q4AYcEKg_5QIV4nNgZlc')

#Create data-base
@bot.message_handler(commands=['start'])
def connect_table(message):
     connect = sqlite3.connect('MemoBase.sql')
     cur =  connect.cursor() 

     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name VARCHAR(50), data TEXT, memo VARCHAR(150))')
     connect.commit()
     cur.close()
     connect.close()
     bot.send_message(message.chat.id, 'Hi! What\'s your name?')
     bot.register_next_step_handler(message, user_name)

def user_name(message):
     name = message.text.strip()
     bot.send.message(message.chat.id, 'Write me date when i should remind you in format DD-MM-YY')
     bot.register_next_step_handler(message, date_add)

def date_add(message):
     date = message.text.strip()
     bot.send.message(message.chat.id, 'Write me your memo')
     bot.register_next_step_handler(message, memo_add)

def memo_add(message):
     memo = message.text.strip()
     connect = sqlite3.connect('MemoBase.sql')
     cur =  connect.cursor() 

     cur.execute('INSERT INTO users(name, date, memo) ')
     connect.commit()
     cur.close()
     connect.close()


#Buttom with sponsorship:
def btn_sponsorship():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Sponsor this project', 'https://github.com/zlobinstas'))
    return markup
#for using it: use reply_markup at the methods 'reply_to' or 'send_message'


#Buttoms with functions add and edit like menu
@bot.message_handler(commands=['start'])
def menu(message): 
     markup = types.ReplyKeyboardMarkup()
     add_btn = types.KeyboardButton('new memo')
     edit_btn = types.KeyboardButton('edit your last memo')
     markup.row(add_btn, edit_btn)
     bot.send_message(message.chat.id, 'Hi! Select your option ', reply_markup=markup)
     bot.register_next_step_handler(message,  on_click)

def on_click(message):
     if message.text == "new memo":
          bot.send_message(message.chat.id, 'Write your memo in format: DD-MM-YY = Your memo') 


#Buttoms with functions add and edit your memo after message
@bot.message_handler(commands=['menu'])
def menu(message):
     markup = types.InlineKeyboardMarkup()
     add_btn = types.InlineKeyboardButton('new memo', callback_data='add')
     edit_btn = types.InlineKeyboardButton('edit your last memo', callback_data='edit')
     markup.row(add_btn, edit_btn)
     bot.send_message(message.chat.id, '.', reply_markup=markup)



#Decorator of callback's actions
@bot.callback_query_handler(func=lambda callback:True)
def callback_add(callback):
     if callback.data == "edit":
          bot.edit_message_text('Edit your memo', callback.message.chat.id, callback.message.message_id)

@bot.message_handler(commands=['site', 'website'])
def site(message):
     webbrowser.open('https://github.com/zlobinstas')

@bot.message_handler(commands=['start'])
def welcome(message):
     bot.send_message(message.chat.id, f"Hi, {message.from_user.first_name} {message.from_user.last_name}!\nPlease, write me your notification in format:\n 'DD-MM-YY = My notification'\n\nFor example: 03-02-2022 = Create new Telegram Bot", reply_markup=btn_sponsorship()) 

bot.polling(non_stop=True) 