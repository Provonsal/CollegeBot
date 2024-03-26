import math
from typing import Any
import telebot
from text_parser import get_text

class SectionChooser():

    def __init__(self, bot: Any, call: Any, info):
        
        """"""
        
        # полученные переменные при создании экземпляра класса
        self.bot: Any = bot
        self.call: Any = call

        self.info = info

        self.parent: str = info.parent
        
        self.number: int = info.number
        
        # дополнительные переменные полученные из предыдущих переменных
        self.back_page: int = info.page
        self.chat_id: int = call.message.chat.id
        self.message_id: int = call.message.message_id
        
        self.text: str = info.text
        
        self.url: list = info.urls
        self.text_url: list = info.url_text
        
        
    def get_menu_buttons(self, menu_buttons_generated: list) -> list:
        
        """
        Функция добавляет дополнительные кнопки для раздела если они имеются, все кнопки - кнопки-ссылки
        """
        if self.text_url != None and self.url != None:
            for text, url in zip(self.text_url, self.url):
                menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text, url=url))
        return menu_buttons_generated

    def add_buttons(self, menu_buttons_generated: list, next_menu: Any) -> Any:
        
        """
        Функция добавляет созданные ранее кнопки, хранящиеся в листе, в экземпляр клавиатуры
        """
        
        for i in menu_buttons_generated:

            next_menu.add(i)
        return next_menu
        
    def create_buttons(self) -> Any:
        
        """
        Функция создает клавиатуру с кнопками управления страницами, возвращает объект клавиатуры
        """

        next_menu: Any = telebot.types.InlineKeyboardMarkup(row_width=1)
        
        menu_buttons_generated: list = self.get_menu_buttons(list())
        
        call_back_data: str = f"{self.parent}``{self.back_page}"
        
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data=call_back_data)) 
        menu_buttons_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='aaa``1'))
        
        next_menu: Any = self.add_buttons(menu_buttons_generated, next_menu) 
        
        return next_menu
        
    def section_selector(self):
        
        """
        Редактирует сообщение, тем самым "открывает" раздел, меняет текст сообщения, добавляет кнопки
        возврата в прошлое меню и глав меню
        """

        self.bot.edit_message_text(
                                    self.text,
                                    self.chat_id,
                                    self.message_id,
                                    reply_markup=self.create_buttons()
                                    )