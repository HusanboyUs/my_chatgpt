#telegram bot here
from model import ChatGPTModel
from telebot import telebot
from decouple import config

TOKEN=config('TOKEN')
bot=telebot.TeleBot(TOKEN, parse_mode='HTML')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Welcome to CHATGPT')


@bot.message_handler(func=lambda message:True)
def echo_message(message):
    model=ChatGPTModel(message.text)
    bot.reply_to(message,str(model.main()))
    

bot.polling()