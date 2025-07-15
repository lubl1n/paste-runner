import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Налаштування
API_DEV_KEY = '#'        # dev ключ
API_USER_KEY = '#'       # user ключ. якщо відсутній, то спочатку потрібно отримати його через get_api_user_token.py
PASTEBIN_API_URL = 'https://pastebin.com/api/api_post.php'    # без змін
TELEGRAM_BOT_TOKEN = '#'  # токен ТГ бота

# Обробка повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if not text or text.strip() == "":
        await update.message.reply_text("Ви повинні надіслати текст для створення пасти.")
        return 

    payload = {
        'api_dev_key': API_DEV_KEY,
        'api_user_key': API_USER_KEY,
        'api_option': 'paste',
        'api_paste_code': text,
        'api_paste_private': '0',             # 0 = public \ 1 = unlisted \ 2 = private
        'api_paste_expire_date': '1H',        # термін дії: 1H, 1D, 1W, 1M або N (безстроково)
        'api_paste_format': 'javascript',     # синтаксис javascript
        'api_paste_name': '✅ FREE PASTE BOT' # назва пасти
    }

    try:
        response = requests.post(PASTEBIN_API_URL, data=payload, timeout=10)
        if response.status_code == 200 and response.text.startswith('http'):
            await update.message.reply_text(f"Паста створена:\n{response.text}")
        else:
            await update.message.reply_text(f"Помилка з боку Pastebin:\n{response.text}")
    except Exception as e:
        await update.message.reply_text(f"Виникла помилка під час створення пасти:\n{str(e)}")

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Надішліть текст — і бот опублікує його як публічну пасту на Pastebin."
    )

# Запуск бота
def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == '__main__':
    main()
