from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6088826318:AAG1pwgzExyFJATsM3u-cmj1r4wtrgkpTVw").build()

app.add_handler(CommandHandler("hello", hello))
print('Заработал!!!')

app.run_polling()