# coding=utf-8 

from tbot import bot
from tbot import current_time
import telebot


class abitur_menu():
    
    def elif_abitur(call):

        def menu_page1(call): # страница меню абитуриента 1
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('О колледже', callback_data="about")
            button_2 = telebot.types.InlineKeyboardButton('Специальности', callback_data="specials")
            button_3 = telebot.types.InlineKeyboardButton('Документы для поступления', callback_data="docum")
            button_4 = telebot.types.InlineKeyboardButton('Как поступить?', callback_data="kak_postup")
            button_5 = telebot.types.InlineKeyboardButton('Стоимость обучения и скидки', callback_data="cost")
            
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Abitur_page2')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4,button_5, page_next, back)
           
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Абитуриента/Родителя абитуриента\nСтраница номер: 1️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu) 
        def menu_page2(call): # страница меню абитуриента 2
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Вступительные испытания', callback_data="exams")
            button_2 = telebot.types.InlineKeyboardButton('Дополнительное образование', callback_data="dop_degree")
            button_3 = telebot.types.InlineKeyboardButton('Внеучебные траектории и клубы', callback_data="clubs_abitur")
            button_4 = telebot.types.InlineKeyboardButton('Лицензия и аккредитация', callback_data="license1")
            button_5 = telebot.types.InlineKeyboardButton('Партнеры колледжа', callback_data="partnership")
            
            page_next = telebot.types.InlineKeyboardButton(text='➡️ Следующая страница ➡️', callback_data='Abitur_page3')
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Abitur_page1')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4, button_5, page_back,page_next, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Абитуриента/Родителя абитуриента\nСтраница номер: 2️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def menu_page3(call): # страница меню абитуриента 3
            
            # определение бот глобальной переменной чтобы мы могли ей воспользоваться и ссылаться
            global bot
            
            # определение объекта клавиатуры с кнопками
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            # определение кнопок для клавиатуры
            button_1 = telebot.types.InlineKeyboardButton('Афиша мероприятий', callback_data="affisha")
            button_2 = telebot.types.InlineKeyboardButton('Кураторы и наставники', callback_data="kuratori")
            button_3 = telebot.types.InlineKeyboardButton('Как добраться?', callback_data="way")
            button_4 = telebot.types.InlineKeyboardButton('Оплатить обучение', callback_data="transac")
            button_5 = telebot.types.InlineKeyboardButton('Наш сайт и социальные сети', callback_data="links1")
            
            page_back = telebot.types.InlineKeyboardButton(text='⬅️ Предыдущая страница ⬅️', callback_data='Abitur_page2')
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            # добавление кнопок к клавиатуре
            next_menu.add(button_1,button_2,button_3,button_4, button_5, page_back, back)
            
            # редактирование сообщения с добавлением к нему кнопок
            bot.edit_message_text('Меню для Абитуриента/Родителя абитуриента\nСтраница номер: 3️⃣ ', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        
        
        # словарь заменяющий длинную цепь if,elif,elif,elif
        abitur_page = {'Abitur_page1':menu_page1,
                     'Abitur_page2':menu_page2,
                     'Abitur_page3':menu_page3,
                     }       
        
        if call.data in abitur_page:
            
            abitur_page[call.data](call)
            bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Открыл страницу <{}> меню Абитуриента/Родителя абитуриента'.format(current_time, call.from_user.id, call.from_user.first_name, call.from_user.last_name,call.from_user.username, call.data))



