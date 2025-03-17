from telegram.ext import Application
from flask import Flask
from threading import Thread
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8000)

def start_bot():
    bot_app = Application.builder().token(BOT_TOKEN).build()
    # أضف ال handlers هنا (مثل CommandHandler)
    bot_app.run_polling()

if __name__ == "__main__":
    Thread(target=run_flask).start()
    start_bot()
    
if __name__ == "__main__":
    # احذف هذين السطرين إذا كنت تستخدم Gunicorn:
    # Thread(target=run_flask).start()
    # start_bot()
    
    # أضف هذا السطر بدلًا منهما:
    app.run(host='0.0.0.0', port=8000)
