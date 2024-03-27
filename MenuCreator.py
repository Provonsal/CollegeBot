# coding=utf-8 

import math
from typing import Any, NoReturn
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tbot import Info


class MenuFromCall():
    
    bot: TeleBot 
    chat_id: int
    message_id: int
    number_in_sqare: tuple
    generated_buttons: list
    next_menu: InlineKeyboardMarkup
    page: int
    info: Info
    parent: str
    callbacks: tuple
    names: tuple
    back_page: int
    max_page: int
    min_page: int

    def __init__(self, bot: TeleBot, call: Any, info: Info, wanted_page: int):

        """
        
        Класс для формирования страниц с кнопками и управления страницами

        """

        self.bot: bot = bot
        self.chat_id: int = call.message.chat.id
        self.message_id: int = call.message.message_id
        
        self.number_in_sqare: tuple = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        
        self.generated_buttons: list = list()
        self.next_menu: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1)
        self.page: int = int(wanted_page)
        
        self.info: Info = info
        self.parent: str = info.parent
        self.callbacks: tuple = info.callbacks
        self.names: tuple = info.names
        self.back_page: int = info.page
        self.max_page: int = math.ceil(len(info.buttons) / 6)
        self.min_page: int = 1
        
    
    def get_buttons(self,  menu: tuple) -> tuple:
        
        """
        Функция возвращает срез списка кнопок для конкретной страницы состоящий до 6 штук
        """
        
        temp: int = 6*self.page
        menu: tuple = tuple(menu[temp-6:temp])
        
        return menu
    
    def create_buttons(self) -> list:

        """
        Функция итерирует список с текстами для кнопок и список с их 
        коллбеками, на каждой итерации создает экземпляр кнопки InlineKeyboardButton
        и добавляет его к списку

        Возвращает список экземпляров классов кнопок InlineKeyboardButton
        """

        menu: list = list()
        for text, callback in zip(self.names, self.callbacks):
            menu.append(InlineKeyboardButton(text, callback_data=f'{callback}``1'))
        return menu

    def control_buttons(self, min_page: int, max_page: int) -> tuple:
        
        """
        Функция возвращает двумерный кортеж с экземплярами кнопок InlineKeyboardButton 
        для управления страницами и кнопку возврата в глав меню
        """

        shablon: str = self.info.callback

        block: InlineKeyboardButton = InlineKeyboardButton(
                                                            text='⛔️', 
                                                            callback_data='None'
                                                            )
        left: InlineKeyboardButton = InlineKeyboardButton(
                                                            text='⏪', 
                                                            callback_data=f'{shablon}``{self.page - 1}'
                                                            )
        right: InlineKeyboardButton = InlineKeyboardButton(
                                                            text='⏩', 
                                                            callback_data=f'{shablon}``{self.page + 1}'
                                                            )
        begining: InlineKeyboardButton = InlineKeyboardButton(
                                                            text='⏮', 
                                                            callback_data=f'{shablon}``{min_page}'
                                                            )

        if self.parent is not None:
            navigation_buttons: tuple = (
                                        InlineKeyboardButton(
                                                            text='🔙 Назад 🔙', 
                                                            callback_data=f'{self.parent}``{self.back_page}'
                                                            ),
                                        InlineKeyboardButton(
                                                            text='📱 В меню 📱', 
                                                            callback_data='aaa``1'
                                                            )
                                        )
        else:
            navigation_buttons: tuple = ()
        if max_page > 1:
            if self.page == min_page:
                arrows: tuple = (block, right)
            elif self.page == max_page:
                arrows: tuple = (left, begining)
            else:
                arrows: tuple = (left,right)
             
            return (arrows, navigation_buttons)  
        return ((),navigation_buttons)

    def add_buttons_to_keyboard(
                                self, menu_page: tuple, 
                                navigation_buttons: tuple, 
                                next_menu: InlineKeyboardMarkup
                                ) -> InlineKeyboardMarkup:

        """
        Функция добавляет кнопки созданной 
        страницы в объект клавиатуры InlineKeyboardMarkup
        """
        
        next_menu.add(*menu_page)
        next_menu.row(*navigation_buttons[0])
        next_menu.add(*navigation_buttons[1])
        
        return next_menu
        

    def pager(self) -> InlineKeyboardMarkup:
        
        """
        Функция которая создает "страницу" кнопок

        Возвращает клавиатуру с набором нужных кнопок
        """

        menu: list = self.create_buttons()
        
        menu_page: tuple = self.get_buttons(menu)

        navigation_buttons: tuple = self.control_buttons(navigation_buttons, self.min_page, self.max_page)

        next_menu: InlineKeyboardMarkup = self.add_buttons_to_keyboard(menu_page, navigation_buttons, self.next_menu)
        
        return next_menu

    def bot_menu_pager(self) -> NoReturn: 
        
        """
        Функция редактирует сообщение, изменяет инлайн кнопки и текст сообщения
        """
        
        menu: InlineKeyboardMarkup = self.pager()

        text: str = f'{self.info.text}\nСтраница номер: {self.number_in_sqare[self.page-1]}' if self.max_page > 1 else self.info.text

        
        self.bot.edit_message_text(
                                text,
                                self.chat_id,
                                self.message_id,
                                reply_markup=menu
                                )
        
        
class MenuFromMessage(MenuFromCall):
    def __init__(self, bot, info, message, wanted_page):
        self.bot: Any = bot
        self.chat_id: int = message.chat.id
        self.message_id: int = message.message_id
        
        self.number_in_sqare: tuple = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        
        
        self.generated_buttons: list = list()
        self.next_menu: Any = InlineKeyboardMarkup(row_width=1)
        self.page: int = int(wanted_page)
        
        self.info = info
        self.parent = info.parent
        self.callbacks = info.callbacks
        self.names = info.names
        self.back_page = info.page
        self.max_page = math.ceil(len(info.buttons) / 6)
        self.min_page = 1

    def bot_menu_pager(self) -> NoReturn:
        """
        Функция создает страницу из кнопок в сообщении
        """
        

        text = f'{self.info.text}\nСтраница номер: {self.number_in_sqare[self.page-1]}' if self.max_page > 1 else self.info.text

        menu = self.pager()
        
        self.bot.send_message(self.chat_id,
                              text,
                              reply_markup=menu)