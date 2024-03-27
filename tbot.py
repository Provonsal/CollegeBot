# coding=utf-8 

import os
from telebot import TeleBot
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

bot: TeleBot = TeleBot(os.getenv("TOKEN"))

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time







