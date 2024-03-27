# coding=utf-8 
import os
import math
import json
from telebot import TeleBot
from datetime import datetime, timedelta
from dotenv import load_dotenv
from typing import Any, NoReturn

load_dotenv()

bot: TeleBot = TeleBot(os.getenv("TOKEN"))

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time



class Info():
    
    callback: str
    parent: str
    text: str
    buttons: dict
    urlButtons: dict
    callbacks: tuple
    names: tuple
    urls: tuple
    url_text: tuple
    number: list
    page: int

    def __init__(self, callback: str):

        with open('settings/settings.json', 'r') as file:
            data = json.load(file)
        
        self.callback: str = callback

        self.parent: str = data[callback]['Parent']
        self.text: str = data[callback]['Text']
        self.buttons: dict = data[callback]['Buttons']
        self.urlButtons: dict = data[callback]['urlButtons']

        self.callbacks: tuple = tuple(self.buttons.keys()) if self.buttons is not None else None
        self.names: tuple = tuple(self.buttons.values()) if self.buttons is not None else None

        self.urls: tuple = tuple(self.urlButtons.keys()) if self.urlButtons is not None else None
        self.url_text: tuple = tuple(self.urlButtons.values()) if self.urlButtons is not None else None

        self.number: list = list(data[self.parent]['Buttons'].keys()).index(callback) if self.parent != None else 0
        self.page: int = math.ceil((self.number+1)/6)



