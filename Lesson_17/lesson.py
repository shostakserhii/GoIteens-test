"""telegram bot who works with NBU API"""

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

TOKEN = '5109879811:AAHhjXil990ryl0C4eCF5oM3DEjFojl0lxQ'
print("Bot is up")
updater = Updater(TOKEN)


def welcome(update, context):
    chat = update.effective_chat
    buttons = [[KeyboardButton('USD')], [KeyboardButton('EUR')], [KeyboardButton('PLN')], [KeyboardButton('GEL')]]
    context.bot.send_message(chat_id=chat.id, text='Hello! I am your currency bot',
                             reply_markup=ReplyKeyboardMarkup(buttons))


def currency_rate(update, context):
    chat = update.effective_chat
    currency_code = update.message.text
    if currency_code in ('USD', 'EUR', 'PLN', 'GEL'):
        currency_rate = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode='
                                     f'{currency_code}&date=20200302&json').json()
        rate = currency_rate[0]['rate']
        message = f'{currency_code} rate: {rate} UAH'
    context.bot.send_message(chat_id=chat.id, text=message)


disp = updater.dispatcher
disp.add_handler(CommandHandler('start', welcome))
disp.add_handler(MessageHandler(Filters.all, currency_rate))

updater.start_polling()
updater.idle()
