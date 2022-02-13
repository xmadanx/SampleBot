from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater('5155754757:AAGHPpySj_7Zx1qmZD2eY9jTW98Co6fESNo')

updater.dispatcher.add_handler(CommandHandler('start', hello))

updater.start_polling()
updater.idle()