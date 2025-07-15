import requests
from typing import Final

from telegram import Update
from telegram.ext import Application, filters, MessageHandler, CommandHandler, ContextTypes

BOT_TOKEN: Final = '7617059268:AAGX1jeRFZHC7BrE20D17iPrpFbMS46r7-s'
BOT_USERNAME: Final = '@crouuus_bot'
CHAT_IDS = [
    "1134816473",  # Ton ID Telegram
]


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
