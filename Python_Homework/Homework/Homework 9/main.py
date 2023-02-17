from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6055258665:AAG9G4OQZvtUJKG76S2hQz-XvRnuCijwVgY").build()

app.add_handler(CommandHandler("hello", hello))
print("Server start")

app.run_polling()