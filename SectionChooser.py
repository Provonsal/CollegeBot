from typing import Any, NoReturn
from telebot import TeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tbot import Info

class SectionChooser():

    bot: TeleBot
    call: Any
    info: Info
    parent: str
    number: int
    next_menu: InlineKeyboardMarkup
    back_page: int
    chat_id: int
    message_id: int
    text: str
    urls: tuple
    text_urls: tuple

    def __init__(
                self, 
                bot: TeleBot, 
                call: Any, 
                info: Info
                ):
        
        """
        Класс что открывает раздел, его текст и кнопки-ссылки
        """
    
        self.bot: TeleBot = bot
        self.call: Any = call

        self.info: Info = info

        self.parent: str = info.parent
        self.number: int = info.number
        self.next_menu: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=1)
        self.back_page: int = info.page
        self.chat_id: int = call.message.chat.id
        self.message_id: int = call.message.message_id
        
        self.text: str = info.text
        
        self.urls: tuple = info.urls
        self.text_urls: tuple = info.url_text
        
        
    def get_menu_buttons(self) -> tuple:
        
        """
        Функция добавляет дополнительные кнопки для раздела если они имеются, все кнопки - кнопки-ссылки
        """

        menu_buttons: list = []

        if self.text_urls != None and self.urls != None:
            for text, url in zip(self.text_urls, self.urls):
                menu_buttons.append(InlineKeyboardButton(text, url=url))
        return tuple(menu_buttons)

    def add_buttons(
                    self,navigation_buttons: tuple,
                    menu_buttons: list, 
                    next_menu: InlineKeyboardMarkup
                    ) -> InlineKeyboardMarkup:
        
        """
        Функция добавляет созданные ранее кнопки, хранящиеся в кортежах, в экземпляр клавиатуры
        """
        next_menu.add(*menu_buttons, *navigation_buttons)
        return next_menu

    def get_navigation_buttons(self) -> tuple:
        call_back_data: str = f"{self.parent}``{self.back_page}"
        
        navigation_buttons: tuple = (
                                    InlineKeyboardButton('🔙 Назад 🔙', callback_data=call_back_data),
                                    InlineKeyboardButton(text='📱 В меню 📱', callback_data='aaa``1')
                                     )
        return navigation_buttons

    def create_buttons(self) -> InlineKeyboardMarkup:
        
        """
        Функция создает клавиатуру с кнопками управления страницами, возвращает объект клавиатуры
        """

        menu_buttons: tuple = self.get_menu_buttons()
        
        navigation_buttons: tuple = self.get_navigation_buttons()
        
        next_menu: InlineKeyboardMarkup = self.add_buttons(
                                                        navigation_buttons, 
                                                        menu_buttons, 
                                                        self.next_menu
                                                        ) 
        
        return next_menu
        
    def section_selector(self) -> NoReturn:
        
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