from code0 import *
import json
import requests


# Telegram API bot token
TOKEN = ""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(bot, update):
    update.message.reply_text("How can I help you?")

def QueryProcess(bot, update):
    reply0=Query1(update.message.text)
    update.message.reply_text(reply0)

def main():

    # Create Updater object and attach dispatcher to it
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    print("Bot started")
    
    # Add command handler to dispatcher
    start_handler = CommandHandler('start',start)
    upper_case = MessageHandler(Filters.text, QueryProcess)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(upper_case)
    
    # Start the bot
    updater.start_polling()
    
    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
