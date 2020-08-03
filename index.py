from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Tokens.TelegramConfig import token

import Scraper

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Diga-me, quer saber o que encareceu, barateou ou manteve com preço igual?')
    update.message.reply_text('/encareceu')
    update.message.reply_text('/barateou')
    update.message.reply_text('/manteve')

def help_command(update, context):
    """Send a message when the command /help is issued."""
    '''todo'''
    #update.message.reply_text('Help!')
    pass


def default(update, context):
    """the user message."""
    update.message.reply_text("Por favor, escolha uma das opções para que eu possa te dizer o que encareceu, barateou ou manteve com o mesmo valor:")
    update.message.reply_text('/encareceu')
    update.message.reply_text('/barateou')
    update.message.reply_text('/manteve')

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
    dp.add_handler(CommandHandler("encareceu", subiu))
    dp.add_handler(CommandHandler("barateou", desceu))
    dp.add_handler(CommandHandler("manteve", igual))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, default))

    updater.start_polling()
    updater.idle()