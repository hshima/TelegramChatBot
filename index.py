from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from Tokens.TelegramConfig import token

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('De onde você vem??')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


if __name__ == "__main__":
    '''
    with open('Tokens/TelegramConfig.json') as f:
        token = json.load(f)'''
    updater = Updater(token, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("start", help_command))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()