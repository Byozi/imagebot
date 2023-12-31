from telegram import Update
from telegram.ext import CallbackContext
from ocrbot.helpers.decorators import send_typing_action

@send_typing_action
def invalid_command(update:Update, context:CallbackContext):
    """
    This function is called when the user enters an invalid command.
    """
    update.message.reply_text("Geçersiz komut. Komut listesi için /help yazın.", quote=True)
