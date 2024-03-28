# coding=utf-8 
import os
import json
import telebot
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

address = os.getenv("ADDRESS")
password, password2 = os.getenv("PASSWORD"), os.getenv("PASSWORD2")
bot = telebot.TeleBot(os.getenv("TOKEN"))

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time







