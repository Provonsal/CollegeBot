# coding=utf-8 

import math
from typing import Any, NoReturn
import telebot
from tbot import current_time


class MenuFromCall():
    
    def __init__(self, bot, call, info, wanted_page):
        self.bot: Any = bot
        self.chat_id: int = call.message.chat.id
        self.message_id: int = call.message.message_id
        
        self.number_in_sqare: tuple = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        
        
        self.generated_buttons: list = list()
        self.next_menu: Any = telebot.types.InlineKeyboardMarkup(row_width=1)
        self.page: int = int(wanted_page)
        
        self.info = info
        self.parent = info.parent
        self.callbacks = info.callbacks
        self.names = info.names
        self.back_page = info.page
        self.max_page = math.ceil(len(info.buttons) / 6)
        self.min_page = 1
        
    
    def sliding_window_listing(self,  menu: list, right_border: int = 6, left_border: int = 0) -> list:
        
        """
        Функция которая скользит по списку с помощью так называемого способа "Скользящего окна", для 
        более подробной информации используйте гугл, задать границы можно при передаче аргументов
        """
        menu_page: list = list()

        for _ in range(self.page):
            menu_page.append(menu[left_border:right_border])
            right_border += 6
            left_border += 6
        return menu_page
    
    def create_buttons(self) -> list:

        """
        Функция итерирует список с текстами для кнопок и список с их коллбеками, после создает экземпляр кнопки
        и добавляет его к списку по которому можно будет итерировать способом скользящего окна

        Возвращает  список кнопок
        """
        menu = list()
        for text, callback in zip(self.names, self.callbacks):
            menu.append(telebot.types.InlineKeyboardButton(text, callback_data=callback+'``1'))
        return menu

    def control_buttons(self,navigation_buttons: tuple, min_page: int, max_page: int, shablon: str) -> tuple:
        
        """
        Функция добавляет кнопки управления страницами и кнопку возврата в глав меню
        """
        block = telebot.types.InlineKeyboardButton(text='⛔️', callback_data='None')
        left = telebot.types.InlineKeyboardButton(text='⏪', callback_data=f'{shablon}``{self.page - 1}')
        right = telebot.types.InlineKeyboardButton(text='⏩', callback_data=f'{shablon}``{self.page + 1}')
        begining = telebot.types.InlineKeyboardButton(text='⏮', callback_data=f'{shablon}``{min_page}')
        if self.parent is not None:
            navigation_buttons = (telebot.types.InlineKeyboardButton(text='🔙 Назад 🔙', callback_data=f'{self.parent}``{self.back_page}'),
                                telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='aaa``1'))
        else:
            navigation_buttons = ()
        if max_page > 1:
            if self.page == min_page:
                arrows = (block, right)
            elif self.page == max_page:
                arrows = (left, begining)
            else:
                arrows = (left,right)
             
            
            return (arrows, navigation_buttons)  
        return ((),navigation_buttons)

    def create_pages(self, menu_page: list) -> tuple:
        
        """
        Функция генерирует, именно генерирует, 6 кнопок для нужной страницы, и дополнительные кнопки меню 
        для управления, такие как перелистывание страниц и возврат в меню и добавляет это все в лист

        Возвращает список кнопок для страницы с определенным номером, который определяется благодаря числу элементов.
        Так что страницы по сути генерируются сами, просто добавьте больше кнопок в список и страницы сами появятся
        
        """
        
        
        menu_buttons_pages_generated: list = [v for i,v in enumerate(menu_page[self.page-1]) if i <= 5]
        
            
        return menu_buttons_pages_generated

    def get_navigation_buttons(self,  min_page: int, max_page: int, ):
        shablon = self.info.callback
        navigation_buttons: list = list()
        navigation_buttons: tuple = self.control_buttons(navigation_buttons, min_page, max_page, shablon)
        return navigation_buttons
    
    def add_buttons_to_keyboard(self, menu_buttons_pages_generated: tuple, navigation_buttons: tuple, next_menu: Any):

        """
        Функция добавляет кнопки созданной страницы в клавиатуру

        """
        
        
        next_menu.add(*menu_buttons_pages_generated)
        next_menu.row(*navigation_buttons[0])
        next_menu.add(*navigation_buttons[1])
        
        return next_menu
        

    def pager(self) -> Any:
        
        """
        Функция которая создает "страницу" кнопок, выясняет максимальную возможную страницу, минимально возможную и тд.

        Возвращает клавиатуру с набором нужных кнопок
        """

        menu = self.create_buttons()
        
        menu_page = self.sliding_window_listing(menu)

        menu_buttons_pages_generated = self.create_pages(menu_page)

        navigation_buttons = self.get_navigation_buttons(self.min_page, self.max_page)

        next_menu = self.add_buttons_to_keyboard(menu_buttons_pages_generated, navigation_buttons, self.next_menu)
        
        return next_menu        

    def bot_menu_pager(self) -> NoReturn: 
        
        """
        Функция создает страницу из кнопок в сообщении
        """
        
        menu = self.pager()

        text = f'{self.info.text}\nСтраница номер: {self.number_in_sqare[self.page-1]}' if self.max_page > 1 else self.info.text

        
        self.bot.edit_message_text(text,
                              self.chat_id,
                              self.message_id,
                              reply_markup=menu)
        
        
class MenuFromMessage(MenuFromCall):
    def __init__(self, bot, info, message, wanted_page):
        self.bot: Any = bot
        self.chat_id: int = message.chat.id
        self.message_id: int = message.message_id
        
        self.number_in_sqare: tuple = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        
        
        self.generated_buttons: list = list()
        self.next_menu: Any = telebot.types.InlineKeyboardMarkup(row_width=1)
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