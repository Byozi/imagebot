from ocrbot.helpers.decorators import send_typing_action
from telegram import Update
from telegram.ext import CallbackContext

@send_typing_action
def start(update:Update,context:CallbackContext):
    """Send a message when the command /start is issued."""
    first=update.effective_user.first_name
    update.message.reply_text('Merhaba! '+str(first)+' \n\nBen Sera Image Bot. Optik Karakter Tanıma Botuyum. \n\nBana net bir resim gönderin ve resimdeki metni tanıyıp bir mesaj olarak göndereceğim!', quote=True)
