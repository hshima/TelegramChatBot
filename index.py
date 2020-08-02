from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Tokens.TelegramConfig import token

import Scraper

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Dia-me, quer saber o que subiu, desceu ou ficou com preço igual?')
    update.message.reply_text('/subiu')
    update.message.reply_text('/desceu')
    update.message.reply_text('/igual')

def help_command(update, context):
    """Send a message when the command /help is issued."""
    '''todo'''
    #update.message.reply_text('Help!')
    pass


def default(update, context):
    """the user message."""
    update.message.reply_text("Por favor, escolha uma das opções para que eu possa te dizer o que subiu, desdeu ou ficou com o mesmo valor:")
    update.message.reply_text('/subiu')
    update.message.reply_text('/desceu')
    update.message.reply_text('/igual')

def subiu(update, context):
    update.message.reply_text(Scraper.subiu())

def desceu(update, context):
    update.message.reply_text(Scraper.desceu())

def igual(update, context):
    update.message.reply_text(Scraper.igual())

if __name__ == "__main__":
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("subiu", subiu))
    dp.add_handler(CommandHandler("desceu", desceu))
    dp.add_handler(CommandHandler("igual", igual))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, default))

    updater.start_polling()
    updater.idle()