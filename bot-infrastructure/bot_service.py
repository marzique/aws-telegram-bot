import os

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')


class BotService:
    def __init__(self):
        self.bot = telebot.TeleBot(BOT_TOKEN)

    def send_message(self, message: str, chat_id: str):
        self.bot.send_message(chat_id=chat_id, text=message)
