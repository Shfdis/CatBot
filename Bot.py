import telebot
from Quiz import *
from QuizInterface import *
from Question import *
from Cat import *
token = '6771976303:AAHU8hmeaCXjBAr21OrV5OaETi6TmeCcqAQ'
bot = telebot.TeleBot(token)
stage = {}
tests = {}
@bot.message_handler(commands=['start'])
def get_text_messages(message):
    global stage
    global tests
    stage.update({message.from_user.id : -1})
    tests.update({message.from_user.id : Test()})
    keyboard = telebot.types.ReplyKeyboardMarkup()
    button1 = telebot.types.KeyboardButton(text="я согласен")
    button2 = telebot.types.KeyboardButton(text="я не согласен")
    keyboard.row(button1)
    keyboard.row(button2)
    bot.send_message(message.from_user.id, tests[message.from_user.id].start(), reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'я твой кот мямямям мя мя мямямям мямя мямямя мя мя':
        keyboard = telebot.types.ReplyKeyboardMarkup()
        bot.send_message(message.from_user.id, "Вы кот", reply_markup=keyboard)
    elif message.text == 'Мыр':
        bot.send_message(message.from_user.id, "Вы мили")
        keyboard = telebot.types.ReplyKeyboardMarkup()
        but = telebot.types.KeyboardButton(text = 'мя')
        keyboard.row(but)
        bot.send_message(message.from_user.id, "Котятки!",  reply_markup=keyboard)
bot.infinity_polling()