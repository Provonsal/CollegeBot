# coding=utf-8 

import math
import telebot
from tbot import current_time


class Menu():
    
    def __init__(self, bot, call, pages, section, page, tree, parent):
        self.bot = bot
        self.call = call
        self.chat_id = call.message.chat.id
        self.message_id = call.message.message_id
        self.section = section
        self.pages = pages
        self.number_in_sqare = ('1️⃣', '2️⃣', '3️⃣', '4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣','🔟')
        self.buttons_text = self.pages[1]
        self.buttons_callback = self.pages[0]
        self.generated_buttons = []
        self.next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
        self.bot = bot
        self.page = page
        self.tree = tree
        self.parent = parent
        
        self.recursion_button = False
        self.personality = {'Stud': 'Студента\Родителя', 
                            'Sotr':'Сотрудника\Преподавателя', 
                            'Abitur':'Абитуриента\Родителя абитуриента'}
    
    def sliding_window_listing(self, menu_page, menu, right_border = 6, left_border = 0):
        
        """
        Функция которая скользит по списку с помощью так называемого способа "Скользящего окна", для 
        более подробной информации используйте гугл, задать границы можно при передаче аргументов
        """

        for i in range(self.page):
            menu_page.append(menu[left_border:right_border])
            right_border += 6
            left_border += 6
        return menu_page
    
    def create_buttons(self, menu):

        """
        Функция итерирует список с текстами для кнопок и список с их коллбеками, после создает экземпляр кнопки
        и добавляет его к списку по которому можно будет итерировать способом скользящего окна

        Возвращает  список кнопок
        """

        for text, callback in zip(self.buttons_text, self.buttons_callback):

            # ВНИМАНИЕ, ЕСЛИ ТЕКСТ КОЛЛБЕКА > 64 БАЙТ ТО ВЫДАСТ ОШИБКУ
            # ЛУЧШЕ ИСПОЛЬЗОВАТЬ АНГЛИЙСКИЕ СИМВОЛЫ, ТАК КАК ОНИ ИСПОЛЬЗУЮТ 1 БАЙТ НА СИМВОЛ
            # В ТО ВРЕМЯ КАК РУССКИЕ ПО 2 БАЙТА НА СИМВОЛ
            

            gggg = f'{self.parent}_{callback}' if self.parent == self.section else f'{self.parent}_{self.section}_{callback}'
            
            
            # расскоментируй строку с принтом если надо проверить коллбек, тип данных коллбека, вес коллбека
            # print(gggg, type(gggg), len(gggg.encode("utf8")), len(self.identity.encode("utf8")), len(callback.encode("utf8")))
            menu.append(telebot.types.InlineKeyboardButton(text, callback_data=gggg))
        return menu
    
    def create_pages(self, min_page, max_page, menu_page):
        
        """
        Функция генерирует, именно генерирует, 6 кнопок для нужной страницы, и дополнительные кнопки меню 
        для управления, такие как перелистывание страниц и возврат в меню и добавляет это все в лист

        Возвращает список кнопок для страницы с определенным номером, который определяется благодаря числу элементов.
        Так что страницы по сути генерируются сами, просто добавьте больше кнопок в список и страницы сами появятся
        """

        menu_buttons_pages_generated = [v for i,v in enumerate(menu_page[self.page-1]) if i <= 5]
        
        shablon = f'{self.section}' if self.parent == self.section else f'{self.parent}{self.tree}{self.section}'
        
        if self.page == min_page:
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{shablon}``{self.page + 1}'))    
        elif self.page == max_page:
            
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{shablon}``{self.page - 1}'))
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='🔄 В начало 🔄', callback_data=f'{shablon}``{min_page}'))
        else:
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data=f'{shablon}``{self.page + 1}'))
            menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data=f'{shablon}``{self.page - 1}'))
            
                    
        menu_buttons_pages_generated.append(telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu'))
        return menu_buttons_pages_generated

    def add_buttons_to_keyboard(self, menu_buttons_pages_generated):

        """
        Функция добавляет кнопки созданной страницы в клавиатуру

        """

        for i in menu_buttons_pages_generated:
            
            self.next_menu.add(i)
        
    def choose_description(self):

        """
        Функция решает какую подпись выбрать для заголовка страницы

        Возвращает строку
        """

        if self.personality.get(self.section) != None:
            self.recursion_button = True
        
        if self.recursion_button:
            text = f'Меню для {self.personality.get(self.parent)}' if self.personality.get(self.parent) != None else ''
        else:
            text = ''
        return text

    def pager(self):
        
        """
        Функция которая создает "страницу" кнопок, выясняет максимальную возможную страницу, минимально возможную и тд.

        Возвращает клавиатуру с набором нужных кнопок
        """

        menu = self.create_buttons(list())
        
        menu_len = len(menu)
        max_page = math.ceil(menu_len / 6)
        min_page = 1
        
        menu_page = self.sliding_window_listing(list(), menu, right_border=6, left_border=0)

        menu_buttons_pages_generated = self.create_pages(min_page, max_page, menu_page)

        self.add_buttons_to_keyboard(menu_buttons_pages_generated)
        
        return self.next_menu        

    def bot_menu_pager(self): 
        
        text = self.choose_description()

        menu = self.pager()
        
        self.bot.edit_message_text(f'{text}\nСтраница номер: {self.number_in_sqare[self.page-1]}',
                              self.chat_id,
                              self.message_id,
                              reply_markup=menu)

    