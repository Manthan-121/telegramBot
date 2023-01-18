import telegram.ext

Token = "5851226941:AAFkHcNsmSTaweIAfnfT4Me9kFTED9PFVy0"

updater = telegram.ext.updater(Token ,use_context=True)
dispacher = updater.dispacher

def start(update,context):
    update.message.reply_text("Hello! Welcome to this Bot")

def help(update,context):
    update.message.reply_text(
        """
        /start -> Welcomt to this bot
        /help -> This perticular message
        /content -> About this bot relatred to content disply
        /python -> The first video from youtube
        /SQL -> The first video from youtube
        /Java -> The first video from youtube
        /contect -> you can redirect from website
        """
    )
def content(update,context):
    update.message.reply_text("We have give the varius project")

def python(update,context):
    update.message.reply_text("You can chose the python")

def SQL(update,context):
    update.message.reply_text("You can chose the SQL")

def Java(update,context):
    update.message.reply_text("You can chose the JAVA")

def contect(update,context):
    update.message.reply_text("You can register using your ID")

dispacher.add_handler(telegram.ext.CommandHandler('start',start))
dispacher.add_handler(telegram.ext.CommandHandler('start',help))
dispacher.add_handler(telegram.ext.CommandHandler('start',content))
dispacher.add_handler(telegram.ext.CommandHandler('start',python))
dispacher.add_handler(telegram.ext.CommandHandler('start',SQL))
dispacher.add_handler(telegram.ext.CommandHandler('start',Java))
dispacher.add_handler(telegram.ext.CommandHandler('start',contect))

updater.star_polling()
updater.idle()
