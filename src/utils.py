import requests
from typing import Final
import os

from telegram import Update
from telegram.ext import Application, filters, MessageHandler, CommandHandler, ContextTypes


BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_IDS = os.environ.get("TELEGRAM_CHAT_IDS", "").split(",")

print(BOT_TOKEN)


def send(text, chat_id):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Message envoyé")
        else:
            print("❌ Erreur lors de l'envoi :", response.text)
    except Exception as e:
        print("❌ Exception :", e)


def send_telegram_message(text):
    for chat_id in CHAT_IDS:
        send(text, chat_id)
        print(f"Message envoyé à {chat_id}: {text}")
