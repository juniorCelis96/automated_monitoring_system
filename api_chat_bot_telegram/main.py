from config import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config

application = ApplicationBuilder().token(config('TOKEN_TELEGRAM_BOT')).build()

async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, ¿cómo estás?")

async def report_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(context.args)
    await update.message.reply_text(context.args[0])

application.add_handler(CommandHandler("start", say_hello))
application.add_handler(CommandHandler("buscar", report_history))

application.run_polling(allowed_updates=Update.ALL_TYPES)