# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

class sotrud():
    
    def elif_sotr():

        def first_str_1(call): # Расписание занятий
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Посмотреть', url='https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748') # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2,button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Посмотреть актуальное расписание занятий можно по ссылке: https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748

Согласовать свое расписание, внести по нему предложения, предупредить о незапланированной ситуации, назначить и согласовать время пересдачи, уточнить возможности аудиторного фонда, попросить маркер и губку можно в кабинете 261. 

Контакты:

Заведующая учебной частью - Лидия Егоровна Пикулина.

Кабинет 261. 
Тел.: 8 (383) 363-63-63, доб.: 1006
E-mail: pikulina-le@opencollege-nsk.ru


Заместитель директора по учебно-методической работе - Юлия Андреевна Хохлова

Кабинет 263. 
Тел.: 8 (383) 363-63-63, доб.: 1005
E-mail: hohlova-ya@opencollege-nsk.ru 
ТГ: @uliahohlova

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_2(call): # Расписание звонков
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Расписание звонков:

    🛎 1 ПАРА С 9:00 ДО 10:30 🛎

    перемена - 10 минут 

    🛎 2 ПАРА С 10:40 ДО 12:10 🛎

    перемена 20 минут

    🛎 3 ПАРА С 12:30 ДО 14:00 🛎

    перемена 20 минут 

    🛎 4 ПАРА С 14:20 ДО 15:50 🛎

    перемена 10 минут

    🛎 5 ПАРА С 16:00 ДО 17:30 🛎

    перемена 10 минут

    🛎 6 ПАРА С 17:40 ДО 19:10 🛎
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_3(call): # Мероприятия
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Афиша мероприятий', url='https://docs.google.com/spreadsheets/d/1BD8GIu3mFyJaGab3cUBPxwgwu6J3KseI/edit?usp=drivesdk&ouid=114275661080998669061&rtpof=true&sd=true') # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2, button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Ближайшие мероприятия колледжа можно посмотреть на нашем сайте в разделе 
“События” https://opencollege-nsk.ru/live/events/и по ссылке в Афише всех мероприятий: https://docs.google.com/spreadsheets/d/1BD8GIu3mFyJaGab3cUBPxwgwu6J3KseI/edit?usp=drivesdk&ouid=114275661080998669061&rtpof=true&sd=true

ТГ канал внеучебной жизни колледжа: t.me/vd_ngok

Если у Вас есть идея мероприятия, вопрос по мероприятию или Вы желаете принять личное участие в событии, Вы можете связаться с заместителем директора по внеучебной деятельности.

Заместитель директора по внеучебной деятельности                                                           

Изотов Алексей Александрович 
Тел.: 8(383)363-63-63, доп.1002
E-mail: vr@opencollege-nsk.ru
ТГ: @aleks_izotov
Кабинет 264 с 11:30 до 20:00

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_4(call): # Дополнительное образование
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Афиша мероприятий', url='https://opencollege-nsk.ru/education/') # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2,button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Вы можете поделиться своим опытом с другими и начать вести курсы дополнительного образования в нашем колледже, и получать дополнительный доход.

Или Вы можете получить дополнительное профессиональное образование по ряду новых направлений и увеличить набор своих компетенций.

Узнать подробнее, записаться на обучение по программам дополнительного образования или создать свой курс можно в отделе дополнительного образования (каб.263) у руководителя направления - Суминой Юлии Александровны с ПН по ПТ с 9:00 до 18:00, или телефону: 8 (905)-934-73-33, а также 8 (383) 363-63-63, добавочный 1012, E-mail.: do@opencollege-nsk.ru ТГ: @yuliyasumina или @ngok_do

Подробнее о программах ДО можно узнать на нашем сайте https://opencollege-nsk.ru/education/
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_5(call): # Получить ведомость
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Получить ведомость на экзамен/ зачет/пересдачу можно в учебном офисе (каб. 267).

Учебный офис можно посетить лично с ПН по ПТ с 9:00 до 18:00 или позвонить по телефону, написать письмо на электронную почту, либо сообщение в электронном журнале.

Контакты для связи
:
для 1-2 курса: 

специалист учебного офиса - Елена Андреевна Козлова
тел.: 8 (383) 363-63-63, добавочный 1008 ;
E-mail: bobrova-ea@opencollege-nsk.ru
для 3-4 курса:
 
специалист учебного офиса - Ирина Валерьевна Лескова                                          
тел.: 8 (383) 363-63-63, добавочный 1007; 
E-mail: leskova-iv@opencollege-nsk.ru

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_6(call): # Доступ в ЭлЖур
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Получить доступ к Электронному журналу можно у заместителя директора по учебно-методической работе (каб. 263).

Контакты для связи:
Заместитель директора по учебно-методической работе
Хохлова Юлия Андреевна
Тел.: 8(383)363-63-63, доп.1005
E-mail: hohlova-ya@opencollege-nsk.ru
ТГ: @uliahohlova
Кабинет 263 с ПН по ПТ с 9:00 до 18:00

Зайти в Электронный журнал НГОК можно по ссылке: https://opencollege-nsk.eljur.ru/authorize, рекомендуем пользоваться браузер-версией.
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_7(call): # Технические сложности
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page2") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Если у Вас возникла сложность связанная с работой компьютерного оборудования, программного обеспечения, интернетом, мультимедиа-проектором и т.д. Вам необходимо обратиться к Системному администратору колледжа.

Контакты:

Системный администратор - Антон Николаевич Козлов 
ТГ: @maykin_a
Кабинет 268

Если у Вас возникла проблема с электричеством, водоснабжением, мебелью, окнами, дверьми и другими хозяйственными моментами. Вам необходимо обратиться к начальнику Административно-хозяйственного отдела.

Контакты:

Начальник АХО - Руслан Алиевич Умхаев
ТГ: 89137490099
Кабинет 165
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_8(call): # Опубликовать пост
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page2") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Вы можете поделиться важной или интересной новостью со всем колледжем. Например, Вы узнали об интересном мероприятии для наших студентов и сотрудников или организовали группой/ сходили на стороннее мероприятие. 

Поделиться информацией о событии и фото/видеоматериалами можно с нашим SMM-менеджером, она примет решение как и когда лучше опубликовать эту новость.

Контакты:

Гордеева Мария Александровна
@gordeevamary
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_9(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_(call): # 
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page1") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        




