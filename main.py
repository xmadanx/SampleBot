from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    update.message.reply_text(f'I am LoveQueenBot and I am here to Share Love <3')

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Mmm..Text to @madan1742')

updater = Updater('5245387008:AAGLGmulUKVsRhcRKgtIubuH9Q8w7aknpEU')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()