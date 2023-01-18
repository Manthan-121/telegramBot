import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_message = "\t👋Hello " + update.effective_chat.first_name + " " + update.effective_chat.last_name + "\nWelcome to this bot \n How can i help you ❓"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=welcome_message)
    keyboard = [['ES', 'EN']]
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""\n
        /start -> Start the bot
        /Help -> Known the command on this bot
        /info -> check the detail
    """)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_name = update.effective_chat.first_name + update.effective_chat.last_name
    await context.bot.send_message(chat_id=update.effective_chat.id, text=chat_name)

if __name__ == '__main__':
    application = ApplicationBuilder().token('5851226941:AAFkHcNsmSTaweIAfnfT4Me9kFTED9PFVy0').build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)
    
    info_handler = CommandHandler('info', info)
    application.add_handler(info_handler)
    
    application.run_polling()