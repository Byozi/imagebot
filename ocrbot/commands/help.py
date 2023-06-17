from telegram import Update
from telegram.ext import CallbackContext
from ocrbot.helpers.decorators import send_typing_action

@send_typing_action
def help(update:Update,context:CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text(
        "Mevcut komut listesi:\
        \n/start - Botu başlatmak için kullanabilirsiniz\
        \n/help - Bu mesajı göstermek için kullanabilirsiniz.",quote=True
    )
