import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Logging setup
logging.basicConfig(level=logging.INFO)

# Load environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
SENTIENT_API_KEY = os.getenv("SENTIENT_API_KEY")

SENTIENT_API_URL = "https://api.fireworks.ai/inference/v1/chat/completions"
MODEL_NAME = "sentientfoundation/dobby-unhinged-llama-3-3-70b-new"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey, I'm Dobby 🤖✨ — your Sentient assistant! Ask me anything.")

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    logging.info(f"User: {user_message}")

    headers = {
        "Authorization": f"Bearer {SENTIENT_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": user_message}],
        "max_tokens": 300,
    }

    try:
        response = requests.post(SENTIENT_API_URL, headers=headers, json=payload)
        data = response.json()
        reply = data.get("choices", [{}])[0].get("message", {}).get("content", "Hmm... I didn’t get that 🤔")
        await update.message.reply_text(reply)
    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("Something went wrong. Try again later!")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))
    app.run_polling()

if __name__ == "__main__":
    main()
