from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os

# الحصول على التوكن من متغيرات البيئة
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبًا! أنا بوتك 🚀")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    await update.message.reply_text(f"لقد أرسلت: {user_text}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))
    
    # بدء البوت
    app.run_polling()

if __name__ == "__main__":
    main()
