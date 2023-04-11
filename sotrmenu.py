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
        def first_str_9(call): # Куратору групп
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page2") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Список кураторов и наставников', url='https://docs.google.com/spreadsheets/d/1b6Lz7k3KT8uDlekmWQZ30HxZ_5jeEll3ERz5uw4bs4M/edit?usp=drivesdk') # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2,button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Если Вы желаете стать куратором учебной группы, Вам необходимо связаться с заместителем директора по внеучебной деятельности.

Заместитель директора по внеучебной деятельности                                                           
Изотов Алексей Александрович 
Тел.: 8(383)363-63-63, доп.1002
E-mail: vr@opencollege-nsk.ru
ТГ: @aleks_izotov
Кабинет 264 с 11:30 до 20:00

Если Вы являетесь куратором группы и у Вас есть вопрос (по планам, мероприятиям, формам отчетов, поощрениях, сложности со студентами и т.д.) - эти вопросы можно уточнить у Алексея Александровича.
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_10(call): # Учебные планы
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page2") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', url='https://opencollege-nsk.ru/sveden/education/eduop/') # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Информацию об описании образовательной программы с приложением образовательной программы в форме электронного документа, в том числе учебные планы можно посмотреть на нашем сайте в сведениях об обрганизации: https://opencollege-nsk.ru/sveden/education/eduop/
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_11(call): # Электронная библиотека
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page2") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Зайти в  библиотеку', url="http://www.iprbookshop.ru/") # кнопка 2
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2,button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Для Вас доступна цифровая библиотека, в которой необходимо зарегистрироваться и, конечно же, не забывать пользоваться не только в учебных, но и в личных целях

ЧТОБЫ ЗАРЕГИСТРИРОВАТЬСЯ:

1️⃣ - Перейдите по ссылке http://www.iprbookshop.ru/

2️⃣ -  Кликните по кнопке «Вход» в правом верхнем углу страницы

3️⃣ - Введите логин и пароль в соответствующие поля
    🔸 ЛОГИН для регистрации пользователей - ngocollege 
    🔹 ПАРОЛЬ - LpNWMfRs

4️⃣ - Выберите тип пользователя «Студент» и заполните свои данные

5️⃣ - Нажмите кнопку «Зарегистрироваться»

Поздравляем, вы в библиотеке!  

Видеоинструкция для регистрации - https://www.youtube.com/watch?v=DexSK_PXMJ8&list=PLRzHZiF2tgd4EPr9O-LF4n8byUDeND5hK&index=8
Видеоинструкция для работы в личном кабинете студента - https://www.youtube.com/watch?v=TTctWlaDXn4&list=PLRzHZiF2tgd4EPr9O-LF4n8byUDeND5hK&index=9

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_12(call): # Связаться со студентом
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page2") # кнопка 1
            button_2 = telebot.types.InlineKeyboardButton('Зайти в  ЭлЖур', url="https://opencollege-nsk.eljur.ru/authorize") # кнопка 2
            button_3 = telebot.types.InlineKeyboardButton('Список кураторов', url="https://docs.google.com/spreadsheets/d/1b6Lz7k3KT8uDlekmWQZ30HxZ_5jeEll3ERz5uw4bs4M/edit?usp=drivesdk") # кнопка 3
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_2,button_3,button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Связаться со студентом, родителем или сотрудником колледжа можно в Электронном журнале НГОК (https://opencollege-nsk.eljur.ru/authorize). 

Для этого Вам необходимо авторизоваться в журнале и написать сообщение студенту, выбрав его в адресатах. В ЭлЖуре Вы можете написать сообщению любому сотруднику или студенту колледжа. 

Также, связаться со студентами 1-го и 2-го курса можно через куратора группы, список кураторов будет доступен при нажатию на кнопку. 
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_13(call): # Сложности со студентами
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page3") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Если у Вас возникла проблема со студентами (не явились на занятие/экзамен), нарушили правила внутреннего распорядка, возникла иная сложная ситуация, Вам необходимо сообщить об этом (при необходимости написать докладную) заместителю директора по учебно-методической работе или заместителю директора по внеучебной деятельности, а они примут дальнейшие решения.

Заместитель директора по учебно-методической работе
Хохлова Юлия Андреевна
Тел.: 8(383)363-63-63, доп.1005
E-mail: hohlova-ya@opencollege-nsk.ru
ТГ: @uliahohlova
Кабинет 263 с 9:00 до 18:00

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
        def first_str_14(call): # Трудоустройство/оплата
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page3") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """По вопросам процесса трудоустройства, а также уточнения по заработной плате, получения справок - можно обратиться к Главному бухгалтеру колледжа. 

Главный бухгалтер
Литвинова Марина Николаевна

Тел.: 8(383)363-63-63, доп.1004
E-mail: buhgalter@opencollege-nsk.ru
Кабинет 274 с ПН по ПТ с 9:00 до 18:00
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_15(call): # Пропускной режим
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page3") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """В нашем колледже действуют пропускной режим, подробнее о нем можно узнать на нашем сайте https://opencollege-nsk.ru/live

* При трудоустройстве Вам оформляется и выдается пропуск, который необходимо предъявить сотруднику службы безопасности при входе в колледж.

Оформить пропуск можно у помощника руководителя. 

Помощник руководителя Кириллова Ольга Константиновна
Тел.: 8(383)363-63-63, доп.1003
E-mail: info@opencollege-nsk.ru
ТГ: @olgkk
Кабинет 252

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_16(call): # Реквизиты колледжа
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page3") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Реквизиты организации: 

Полное наименование: 
Автономная некоммерческая организация среднего профессионального образования "НОВОСИБИРСКИЙ ГОРОДСКОЙ ОТКРЫТЫЙ КОЛЛЕДЖ"

Сокращенное наименование: АНО СПО “НГОК”, НГОК
Расчётный счёт: 40703810744050003777
ИНН: 5404089162
КПП: 540201001
ОГРН/ОГРНИП: 1195476036018
Банк: СИБИРСКИЙ БАНК ПАО СБЕРБАНК
БИК: 045004641
Кор. счёт: 30101810500000000641

Юридический адрес: 630082, Российская федерация, Новосибирская область, г. Новосибирск, ул. 2-я Союза Молодежи, 31
Фактический адрес: 630082, Российская федерация, Новосибирская область, г. Новосибирск, ул. 2-я Союза Молодежи, 31

Директор: Демидов Александр Александрович

И.о. директора: Катрич Ольга Владимировна

Контакты:

info@opencollege-nsk.ru

8 (383) 363-63-63

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_17(call): # Другой вопрос
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page3") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Если у Вас возник иной вопрос, Вы можете обратиться к нашим коллегам: 

Директор колледжа
Катрич Ольга Владимировна 
Тел.: 8(383)363-63-63, доп.1001
E-mail: director@opencollege-nsk.ru
ТГ: @olgakatrish
Кабинет 252

Помощник руководителя
Кириллова Ольга Константиновна
Тел.: 8(383)363-63-63, доп.1003
E-mail: info@opencollege-nsk.ru
ТГ: @olgkk
Кабинет 252

Заместитель директора по учебно-методической работе
Хохлова Юлия Андреевна
Тел.: 8(383)363-63-63, доп.1005
E-mail: hohlova-ya@opencollege-nsk.ru
ТГ: @uliahohlova
Кабинет 263

Заместитель директора по внеучебной деятельности                                                           
Изотов Алексей Александрович 
Тел.: 8(383)363-63-63, доп.1002
E-mail: vr@opencollege-nsk.ru
ТГ: @aleks_izotov
Кабинет 264

Заведующая учебной частью
Пикулина Лидия Егоровна
Тел.: 8 (383) 363-63-63, доб.: 1006
E-mail: pikulina-le@opencollege-nsk.ru
Кабинет 261. 

Руководитель отдела дистанционного обучения
Искендяева Александра Ярославовна
ТГ: @jitnazemle

Специалист центра карьеры, практики и трудоустройства
Панков Антон Олегович
Тел.: 8 (383) 363-63-63, доб.: 1009
E-mail: praktika@opencollege-nsk.ru
ТГ: @antonionsk54
Кабинет 264. 

Руководитель отдела маркетинга
Герасименко Татьяна Николаевна
ТГ: @GeraTN
Кабинет 265. 

Педагог-психолог
Антипина Надежда Матвеевна
ТГ: @antipinapsyandlife
Кабинет 282. 

Руководитель отдела по работе с абитуриентами
Коробкина Марина Александровна
Тел.: 8 (383) 363-63-63, доб.: 1014
E-mail: priem@opencollege-nsk.ru
ТГ: @korobkinamarina
Кабинет 271
"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        def first_str_18(call): # Наш сайт и социальные сети
            
            global bot # объявление переменной глобально чтобы она оказалась в зоне определения
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1) # создание меню
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Sotr_page3") # кнопка 1
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu') # кнопка назад
            
            next_menu.add(button_1, back) # добавление кнопок в меню
            
            # текст сообщения
            text = """Наш сайт: https://opencollege-nsk.ru/

Телеграм канал: t.me/opencollege_nsk

ВКонтакте: https://vk.com/opencollege_nsk

Инстаграм: https://instagram.com/opencollege.nsk

YouTube: https://youtube.com/@opencollege54

Телеграм канал Внеучебной жизни: t.me/vd_ngok

Телеграм канал Центра карьеры и практики: t.me/praktika_ngok


Телеграм канал для Абитуриентов: t.me/opencollege2023

Чат иногородних студентов: t.me/unified_college


ЭлЖур: https://opencollege-nsk.eljur.ru/authorize

* Instagram, продукт компании Meta, которая признана экстремистской организацией в России.

"""
            
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)# редактирование сообщения по его id и прикрепление
                                                         # к сообщению меню с кнопками
        if call.data == "raspis_zanyat": # Расписание занятий
            return first_str_1(call)
        elif call.data == "raspis_zvonkov": # Расписание звонков
            return first_str_2(call)
        elif call.data == "events": # Мероприятия
            return first_str_3(call)
        elif call.data == "dopolnitel_obr": # Дополнительное образование
            return first_str_4(call)
        elif call.data == "vedomost": # Получить ведомость
            return first_str_5(call)
        elif call.data == "dostupElJur": # Доступ в ЭлЖур
            return first_str_6(call)
        elif call.data == "Tech_diff": # Технические сложности
            return first_str_7(call)
        elif call.data == "post": # Опубликовать пост
            return first_str_8(call)
        elif call.data == "kuratoru": # Куратору групп
            return first_str_9(call)
        elif call.data == "plans": # Учебные планы
            return first_str_10(call)
        elif call.data == "electr_lib": # Электронная библиотека
            return first_str_11(call)
        elif call.data == "message_student": # Связаться со студентом
            return first_str_12(call)
        elif call.data == "student_diff": # Сложности со студентами
            return first_str_13(call)
        elif call.data == "trud": # Трудоустройство/оплата
            return first_str_14(call)
        elif call.data == "propusk": # Пропускной режим
            return first_str_15(call)
        elif call.data == "rekvisit": # Реквизиты колледжа
            return first_str_16(call)
        elif call.data == "other_question": # Другой вопрос
            return first_str_17(call)
        elif call.data == "links_sotr": # Наш сайт и социальные сети
            return first_str_18(call)




