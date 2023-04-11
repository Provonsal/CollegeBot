# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

class student():
    
    def elif_stud(call):
        
        def first_str_1(call): # Получить справку
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1")
            button_2 = telebot.types.InlineKeyboardButton('Заказать справку', url="https://opencollege-nsk.ru/live/#extract")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_1, back)
            
            text = """Получить справку (по месту требования) можно в учебном офисе колледжа, для этого необходимо предварительно её заказать. 

Заказать справку можно лично посетив учебный офис (кабинет 267) в рабочее время (с 9:00 до 18:00) или оформив заявку на нашем сайте:  https://opencollege-nsk.ru/live/#extract 

Необходимо указать, куда именно требуется справка: налоговая, место работы, военкомат, другое место.

После заказа справки она будет подготовлена в течение трех рабочих дней.

Уточнить, готова ли она, можно в учебном офисе:

для 1-2 курса: 
специалист учебного офиса - Елена Андреевна Козлова
тел.: 8 (383) 363-63-63, добавочный 1008 ; 
E-mail: bobrova-ea@opencollege-nsk.ru

для 3-4 курса: 
специалист учебного - Ирина Валерьевна Лескова                               
тел.: 8 (383) 363-63-63, добавочный 1007; 
E-mail: leskova-iv@opencollege-nsk.ru

    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2(call): # Получить отсрочку
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1")
            button_2 = telebot.types.InlineKeyboardButton('Заказать справку', url="https://opencollege-nsk.ru/live/#extract")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_1, back)
            
            text = """Получить справку (по месту требования) можно в учебном офисе колледжа, для этого необходимо предварительно её заказать. 

Заказать справку можно лично посетив учебный офис (кабинет 261) в рабочее время (с 9:00 до 18:00) или оформив заявку на нашем сайте:  https://opencollege-nsk.ru/live/#extract, обязательно указав, что справка необходима в военный комиссариат.
После заказа справки она будет подготовлена в течение трех рабочих в течении трех рабочих дней.

Уточнить, готова ли она, можно в учебном офисе у специалиста по ведению воинского учета и военно-патриотической работе – Рудина Андрея Владимировича (каб.261).
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_3(call): # Расписание занятий
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1")
            button_2 = telebot.types.InlineKeyboardButton('Посмотреть расписание', url="https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_1, back)
            
            text = """Посмотреть актуальное расписание занятий можно по ссылке:
https://docs.google.com/spreadsheets/d/1FiMov0r4UUDKT6A56NWMImpoUakDC2YDevgaOpJQ7Qc/edit#gid=1514109748
    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_4(call): # Расписание звонков
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1, back)
            
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
                                  reply_markup=next_menu)
        def first_str_5(call): # Связаться с администрацией
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1, back)
            
            text = """Директор колледжа
Катрич Ольга Владимировна 

Тел.: 8(383)363-63-63, доп.1001
E-mail: director@opencollege-nsk.ru
ТГ: @olgakatrish
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
    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_6(call): # Оплата
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page1")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1, back)
            
            text = """Оплатить обучение можно онлайн! 

График платежей у каждого индивидуальный, посмотреть его можно в приложении к Вашему договору, но если Вы не помните свой график, можно уточнить его в учебном офисе 8 (383) 363-63-63 (доб.1007 или 1008).

Мы точно можем сказать, что если вы платите поквартально, платежи Вы должны внести до: 31 августа, 15 ноября, 15 февраля и 15 апреля. 


ИНСТРУКЦИЯ ПО ОПЛАТЕ ЧЕРЕЗ ПРИЛОЖЕНИЕ СБЕРА (можно оплатить через другое)
1️⃣ Вкладка «Платежи»

2️⃣ В поисковой строке выбираете «Платеж по реквизитам»

3️⃣ Выбираете «Оплата по ИНН» и вводите наш ИНН 5404089162

4️⃣ Заполняете поля «Расчетный счет получателя» и «БИК банка получателя»
Р/с 40703810744050003777
БИК 045004641

5️⃣ В следующей вкладке вы увидите наше наименование АНО СПО "НОВОСИБИРСКИЙ ГОРОДСКОЙ ОТКРЫТЫЙ КОЛЛЕДЖ" - это подтверждение того, что все данные заполнены верно. 

6️⃣ Заполняете ФИО плательщика (ФИО обучающегося или родителя, указанного в договоре) и назначение платежа «Оплата за обучение студента ФИО, № договора»

7️⃣ Вводите сумму

8️⃣ Производите оплату
    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_7(call): # Финансовая задолжность
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data='Stud_page1')
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1, back)
            
            text = """Уточнить Вашу финансовую задолженность и срок оплаты обучения можно в учебном офисе (каб. 267).

Учебный офис можно посетить лично с ПН по ПТ с 9:00 до 18:00 или позвонить по телефону, написать письмо на электронную почту, либо сообщение в электронном журнале.
 
Контакты для связи:

для 1-2 курса: 

специалист учебного офиса - Елена Андреевна Козлова
тел.: 8 (383) 363-63-63, добавочный 1008 ; 
E-mail: bobrova-ea@opencollege-nsk.ru

для 3-4 курса: 

специалист учебного - Ирина Валерьевна Лескова
тел.: 8 (383) 363-63-63, добавочный 1007; 
E-mail: leskova-iv@opencollege-nsk.ru
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_8(call): # Узнать долги/пересдать сессию
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page2")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1, back)
            
            text = """Уточнить Вашу академическую задолженность и возможность пересдать долги по учебным дисциплинам можно в учебном офисе (каб. 267).

Учебный офис можно посетить лично с ПН по ПТ с 9:00 до 18:00 или позвонить по телефону, написать письмо на электронную почту, либо сообщение в электронном журнале.

Контакты для связи:

для 1-2 курса: 

специалист учебного офиса - Елена Андреевна Козлова
тел.: 8 (383) 363-63-63, добавочный 1008 ; 
E-mail: bobrova-ea@opencollege-nsk.ru

для 3-4 курса: 

специалист учебного - Ирина Валерьевна Лескова
тел.: 8 (383) 363-63-63, добавочный 1007; 
E-mail: leskova-iv@opencollege-nsk.ru

*График пересдач зачетов и экзаменов по учебным дисциплинам регулярно размещается в телеграмм канале колледжа и на главном информационном стенде. Перед посещением пересдачи уточните у преподавателя, допущены ли Вы к ней?!
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_9(call): # Заочка
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page2")
            button_2 = telebot.types.InlineKeyboardButton('Перейти в Instudy', url="https://opencollege-nsk.ru/instudy")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_1, back)
            
            text = """Преимущества дистанционного обучения в нашем колледже:
1️⃣ - Всегда на связи
Улучшает коммуникации между студентами, кураторами и преподавателями. Мы общаемся на учебной платформе и в чатах Telegram.

2️⃣ - Доступность
Становится доступным везде, где есть выход в интернет. Студент изучает записанный учебный материал, выполняет задания.

3️⃣ - Индивидуальный подход
Объединяет студентов на вебинарах и онлайн-практикумах. В каждом семестре предусмотрены онлайн-встречи с преподавателями, ответы на вопросы, консультации по курсовым и дипломным работам.

4️⃣ - Трудоустройство
Многие наши студенты трудоустроены по будущей профессии и применяют полученные знания на практике.

Занятия на заочном отделении проходят через собственную образовательную платформу нашего холдинга - “INSTUDY”
Узнать подробнее о том, как проходят занятия и протестировать платформу можно по ссылке: https://opencollege-nsk.ru/instudy/

Если у Вас остались вопросы по заочному обучению, Вы можете написать руководителю отдела дистанционного обучения Александре Ярославовне Искендяевой в телеграме: @jitnazemle
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_10(call): # Практика
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page2")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_1, back)
            
            text = """Подробная информация о прохождении практики располагается на нашем сайте по ссылке: https://opencollege-nsk.ru/live/career/
Сроки прохождения практики можно посмотреть в учебном плане Вашей группы на сайте: https://opencollege-nsk.ru/sveden/education/eduop/

Для тех, кто уже выходит на практику мы составили пошаговый план действий:

1️⃣ Если у Вас есть собственное место для прохождения практики и оно соответствует условиям темы практики, Вам необходимо взять "Карточку организации" с реквизитами и предоставить ее в Центр карьеры, практики и трудоустройства (264 кабинет);
    *Если у Вас нет места прохождения практики, вы будете распределены от колледжа в соответствии с темой практики.

2️⃣ После заключения договора между колледжем и организацией, Вы забираете договор, подписываете его в организации и приносите обратно в 264 кабинет;

3️⃣ Получаете в 264 кабинете комплект документов для прохождения практики (направление, дневник практики).

4️⃣ Проходите практику в установленные учебным планом сроки;

5️⃣ После прохождения практики приносите заполненный (подписанный всеми сторонами) комплект документов обратно в 264 кабинет.

Уточнить конкретный вопрос о прохождении практики, получить направление и заключить договор с партнером (работодателем) можно в Центре карьеры, практики и трудоустройства (каб.264) с ПН по ПТ с 9:00 до 18:00. 

Руководит направлением – Панков Антон Олегович.
Тел.: 8 (383) 363-63-63, добавочный 1009; 
E-mail: praktika@opencollege-nsk.ru

Телеграм канал Центра карьеры НГОК @praktika_ngok
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_11(call): # Афиша
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page2")
            button_2 = telebot.types.InlineKeyboardButton('Афиша мероприятий', url="https://docs.google.com/spreadsheets/d/1BD8GIu3mFyJaGab3cUBPxwgwu6J3KseI/edit?usp=drivesdk&ouid=114275661080998669061&rtpof=true&sd=true")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_1, back)
            
            text = """Ближайшие мероприятия колледжа можно посмотреть на нашем сайте в разделе “События” 
https://opencollege-nsk.ru/live/events/
или в Афише всех ближайших событий по кнопке в меню ⬇️

Новости по мероприятиям можно посмотреть в канале внеучебной жизни t.me/vd_ngok
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_12(call): # Клубы
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page2")
            button_2 = telebot.types.InlineKeyboardButton('Узнать подробнее', url="https://opencollege-nsk.ru/live/extracurricular/?group=creation")
            button_3 = telebot.types.InlineKeyboardButton('Вступить в траекторию', url="https://forms.gle/BLf9EBoycc8EagQx5")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_3,button_1, back)
            
            text = """Параллельно получению образования по своей основной учебной программе, каждый студент колледжа может выбрать любую из внеучебных траекторий, в рамках которой ему будет предложено развивать собственные навыки с использованием ресурсов колледжа.
        
В каждой траектории есть клубы по интересам, в которые можно вступить, а также у каждого студента есть возможность стать членом комитета траектории и заниматься планированием деятельности и развитием всей траектории.

У каждого есть возможность самореализации, совместной работы в команде в роли активиста колледжа, а также управления командой в роли руководителя студенческого клуба или тим-лидера внеучебной траектории.
    
Все студенты могут вступить в неограниченное количество клубов и траекторий, но желательно определить для себя наиболее приоритетную и значимую, в которой дальше профессионально развиваться.

Узнать подробнее о траекториях, клубах и вступить в них можно на нашем сайте, по ссылке:
https://opencollege-nsk.ru/live/extracurricular/?group=creation

ТГ канал внеучебной жизни колледжа: t.me/vd_ngok
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_13(call): # Дополнительное образование или второй диплом
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page2")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/education/")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2, button_1, back)
            
            text = """Ты хочешь развиваться сразу в нескольких направлениях и успеть за студенческие годы как можно больше?

А может, тебе кажется, что ты поступил не совсем туда, и осознание этого пришло уже во время учебы.

Бросать и начинать все заново не хочется – и в этом нет необходимости: ты можешь найти желаемую специализацию в списке программ дополнительного профессионального образования и заниматься параллельно.
Узнать подробнее и записаться на обучение по программам дополнительного образования можно в отделе дополнительного образования (каб.263) у руководителя направления - Суминой Юлии Александровны с ПН по ПТ с 9:00 до 18:00, или телефону: 8 (905)-934-73-33, а также 8 (383) 363-63-63, добавочный 1012.
E-mail: do@opencollege-nsk.ru или в ТГ: @ngok_do

Подробнее о программах ДО можно узнать на нашем сайте https://opencollege-nsk.ru/education/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_14(call): # Дополнительное образование или второй диплом
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page3")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/education/")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2, button_1, back)
            
            text = """Ты хочешь развиваться сразу в нескольких направлениях и успеть за студенческие годы как можно больше?

А может, тебе кажется, что ты поступил не совсем туда, и осознание этого пришло уже во время учебы.

Бросать и начинать все заново не хочется – и в этом нет необходимости: ты можешь найти желаемую специализацию в списке программ дополнительного профессионального образования и заниматься параллельно.
Узнать подробнее и записаться на обучение по программам дополнительного образования можно в отделе дополнительного образования (каб.263) у руководителя направления - Суминой Юлии Александровны с ПН по ПТ с 9:00 до 18:00, или телефону: 8 (905)-934-73-33, а также 8 (383) 363-63-63, добавочный 1012.
E-mail: do@opencollege-nsk.ru или в ТГ: @ngok_do

Подробнее о программах ДО можно узнать на нашем сайте https://opencollege-nsk.ru/education/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_15(call): # Учебные планы
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page3")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/sveden/education/eduop/")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2, button_1, back)
            
            text = """Информацию об описании образовательной программы с приложением образовательной программы в форме электронного документа, в том числе учебные планы можно посмотреть на нашем сайте в сведениях об обрганизации: https://opencollege-nsk.ru/sveden/education/eduop/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_16(call): # Электронная библиотека
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page3")
            button_2 = telebot.types.InlineKeyboardButton('Зайти в библиотеку', url="http://www.iprbookshop.ru/")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2, button_1, back)
            
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
                                  reply_markup=next_menu)
        def first_str_17(call): # Связаться с преподавателем
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page3")
            button_2 = telebot.types.InlineKeyboardButton('Зайти в ЭлЖур', url="https://opencollege-nsk.eljur.ru/authorize")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2, button_1, back)
            
            text = """Связаться с преподавателем или сотрудником колледжа можно в Электронном журнале НГОК (https://opencollege-nsk.eljur.ru/authorize). 

Для этого Вам необходимо авторизоваться в журнале и написать сообщение преподавателю, выбрав его в адресатах. В ЭлЖуре Вы можете написать сообщению любому сотруднику или студенту колледжа. 

* Рекомендуем Вам скачать приложение ЭлЖур на Ваше мобильное устройство.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_18(call): # ЭлЖур
            
            global bot
            
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page3")
            button_2 = telebot.types.InlineKeyboardButton('Зайти в  ЭлЖур', url="https://opencollege-nsk.eljur.ru/authorize")
            
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            
            next_menu.add(button_2,button_1, back)
            
            text = """Получить доступ к Электронному журналу можно в учебном офисе (каб. 267).

Учебный офис можно посетить лично с ПН по ПТ с 9:00 до 18:00 или написать письмо на электронную почту. 

При обращении через электронную почту необходимо указать Ваше ФИО, группу, контактный телефон, если Вы родитель: указать Ваше ФИО, ФИО ребенка, группу ребенка, Ваш контактный телефон.

Контакты для связи:

для 1-2 курса: 

специалист учебного офиса - Елена Андреевна Козлова                                
тел.: 8 (383) 363-63-63, добавочный 1008 ; 
E-mail: bobrova-ea@opencollege-nsk.ru

для 3-4 курса:

специалист учебного - Ирина Валерьевна Лескова                                          
тел.: 8 (383) 363-63-63, добавочный 1007; 
E-mail: leskova-iv@opencollege-nsk.ru
Зайти в Электронный журнал НГОК можно по ссылке: 
https://opencollege-nsk.eljur.ru/authorize, 
рекомендуем Вам скачать приложение ЭлЖур на Ваше мобильное устройство.

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_19(call): # Транспортная карта
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page3")
            button_2 = telebot.types.InlineKeyboardButton('Зайти в  ЭлЖур', url="https://t-karta.ru/novosibirsk/student")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2, button_1, back)
            text = """КАК ПОЛУЧИТЬ ТРАНСПОРТНУЮ КАРТУ СТУДЕНТА?

1️⃣ - необходимо заполнить анкету по ссылке https://t-karta.ru/novosibirsk/student

2️⃣ - распечатать анкету

3️⃣ - приклеить свою фотографию

4️⃣ - оплатить 140 руб. за изготовление карты в терминале "Квартоплат" (при оплате необходимо указать номер анкеты). *Терминалы имеют красно-синие оттенки и стоят в метро

5️⃣ - анкету с фотографией и квитанцию отдать в 264 кабинет в будний день с 11:30 до 19:00.

ЧТО ДАЁТ ТРАНСПОРТНАЯ КАРТА?

1️⃣ - скидку на проезд в общественном транспорте в размере 50%

2️⃣ - или безлимит на поездки в общественном транспорте за фиксированную сумму.

СКОЛЬКО ЖДАТЬ ИЗГОТОВЛЕНИЯ КАРТЫ?

Время изготовления карты от 2-х недель до 2-х месяцев.

    * Что делать если нет принтера для печати анкеты? Анкету можно взять в бумажном виде в каб. 264 и совершить все оставшиеся действия.

По вопросам оформления транспортной карты можно обратиться к заместителю директора по внеучебной деятельности Изотову Алексею Александровичу (264 кабинет) - @aleks_izotov

ЧТО ДЕЛАТЬ ЕСЛИ КАРТА ПЕРЕСТАЛА РАБОТАТЬ?

Транспортную карту нужно регулярно продлевать. Продлить карту можно простым способом - нужно ВНЕСТИ ЛЮБУЮ СУММУ ЧЕРЕЗ ТЕРМИНАЛ “КВАРТОПЛАТ” в ОКТЯБРЕ и АПРЕЛЕ месяце каждого календарного года. 

У выпускников транспортные карты действуют до 31 августа, у отчисленных студентов карты перестают действовать автоматически.

ЧТО ДЕЛАТЬ ЕСЛИ ПОТЕРЯЛ(А) ТРАНСПОРТНУЮ КАРТУ?

1️⃣ Необходимо заказать справку (по месту требования) в учебном офисе (267 кабинет). Подробнее в разделе «Получить справку».

2️⃣ Обратиться (в рабочее время) лично со справкой и студенческим билетом в главный офис “Пассажиртрансснаб” по адресу: Красный проспект, 161 и попросить восстановить Вашу карту. (Понадобится оплата повторного изготовления карты).
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_20(call): # Сотрудники
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page4")
            button_2 = telebot.types.InlineKeyboardButton('Все сотрудники', url="https://opencollege-nsk.ru/college/structure/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2, button_1, back)
            text = """Познакомиться со всеми сотрудниками колледжа можно на нашем сайте:

https://opencollege-nsk.ru/college/structure/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_21(call): # Консультация психолога
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page4")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Если у тебя возникли сложности или тебе нужен совет, консультация психолога, ты можешь записаться на приём к нашему профессиональному психологу.

Контакты:

Педагог-психолог
Надежда Матвеевна Антипина 

ТГ: @antipinapsyandlife
Кабинет 282, ВТ и ПТ.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_22(call): # Самоконтроль
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page4")
            button_2 = telebot.types.InlineKeyboardButton('Подробнее о совете', url="https://opencollege-nsk.ru/live/association/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Совет обучающихся — единственный постоянно действующий представительный и координирующий орган всех студентов колледжа, центр студенческого самоуправления, работающий на благо студентов со дня основания колледжа.

Мы помогаем в организации внеучебной жизни в колледже, реализовываем социально значимые студенческие инициативы, содействуем раскрытию потенциала и формированию новых навыков у студентов в творческих, спортивных и образовательных направлениях. Помогаем в решении образовательных, социальных и бытовых проблем, защищаем права и представляем законные интересы студентов перед органами управления, а также стараемся сделать всё возможное, чтобы каждый обучающийся чувствовал себя комфортно в стенах нашего колледжа.

Структура совета:
Председатель совета, тим-лидер траектории "Познание мира и саморазвитие"

Тимощик Виктория Алексеевна 
@sstrawberrrrry

Заместитель председателя, тим-лидер траектории "Медиа и технологии"

Баркина Софья Андреевна
@sofi_brkn

Секретарь совета, тим-лидер траектории "Лидерство и инициативы"

Отт Дарья Сергеевна
@daryaott

Тим-лидер траектории"Творчество и культура"

Янушевская Диана Сергеевна
@m_dvsk

Тим-лидер траектории "ЗОЖ и спорт"

Сухих Кристина Андреевна
@blissfulsun

Тим-лидер совета старост

Семченкова Дарья Антоновна
@dasha_really_pretty
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_23(call): # Потерял\нашел вещь
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page4")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Если Вы потеряли или нашли чью-то вещь, Вам необходимо обратиться на пост охраны и передать чужую или спросить свою вещь. На посту охраны хранятся потерянные вещи. Если это не даст результатов, можно попробовать написать о ситуации в наш общий чат 
        
    https://t.me/opencollege_nsk
    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_24(call): # Правила внутреннего распорядка
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page4")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/live/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2, button_1, back)
            text = """В нашем колледже действуют правила внутреннего распорядка, подробнее о них можно узнать на нашем сайте https://opencollege-nsk.ru/live/
    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_25(call): # Пропускной режим
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page4")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/live")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """В нашем колледже действуют пропускной режим, подробнее о нем можно узнать на нашем сайте https://opencollege-nsk.ru/live

*Главное правило - всегда носи с собой студенческий билет!
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_26(call): # Скидки и виды поощрений
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page5")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """На данный момент в нашем колледже идёт процесс разработки возможных скидок и образовательных грантов для наших студентов. Образовательные гранты мы планируем начать выдавать в 2023-2024 учебном году. Подробные условия получения гранта будут опубликованы позже.
    """
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_27(call): # Другой вопрос
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page5")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Если Ваш вопрос связан с учебным процессом, например, Вы заболели и хотите зачесть пропуски по уважительной причине, потеряли студенческий билет, хотите написать объяснительную, желаете перевестись к нам в колледж, перевестись от нас или отчислиться, узнать график платежей, написать заявление на отсрочку платежа, заключить дополнительное соглашение к договору, у Вас возникли сложности с освоением образовательной программы и другое, Вам необходимо обратиться в учебный офис.

Учебный офис (кабинет 267) работает по будням с 9:00 до 18:00. 

Контакты:

для 1-2 курса: 
специалист учебного офиса - Елена Андреевна Козлова
тел.: 8 (383) 363-63-63, добавочный 1008 ; 
E-mail: bobrova-ea@opencollege-nsk.ru

для 3-4 курса: 
специалист учебного - Ирина Валерьевна Лескова                               
тел.: 8 (383) 363-63-63, добавочный 1007; 
E-mail: leskova-iv@opencollege-nsk.ru

Если Ваш вопрос не связан с учебной деятельностью или он более сложный и Вы не смогли его решить в учебном офисе, Вы можете обратиться к заместителю директора по учебно-методической работе - 

Юлии Андреевне Хохловой 
(кабинет 263, тел.: 8 (383) 363-63-63, добавочный 1005) 

или заместителю директора по внеучебной деятельности - 

Алексею Александровичу Изотову 
(кабинет 264, тел.: 8 (383) 363-63-63, добавочный 1002).
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_28(call): # Ссылки
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Stud_page5")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Наш сайт: https://opencollege-nsk.ru/

Телеграм канал: https://t.me/opencollege_nsk

ВКонтакте: https://vk.com/opencollege_nsk

Инстаграм: https://instagram.com/opencollege.nsk

YouTube: https://youtube.com/@opencollege54

Телеграм канал Внеучебной жизни: https://t.me/vd_ngok

Телеграм канал Центра карьеры и практики: https://t.me/praktika_ngok

Телеграм канал для Абитуриентов: https://t.me/opencollege2023

Чат иногородних студентов: https://t.me/unified_college

ЭлЖур: https://opencollege-nsk.eljur.ru/authorize

* Instagram, продукт компании Meta, которая признана экстремистской организацией в России.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        if call.data == "spravka": # Получить справку
            first_str_1(call)
        elif call.data == "otsrochka": # Получить отсрочку
            first_str_2(call)
        elif call.data == "rasp zanyat": # Расписание занятий
            first_str_3(call)
        elif call.data == "rasp zvon": # Расписание звонков
            first_str_4(call)
        elif call.data == "message_admin": # Связаться с администрацией
            first_str_5(call)
        elif call.data == "oplata": # Оплата
            first_str_6(call)
        elif call.data == "dolg_money": # Финансовая задолжность
            first_str_7(call)
        elif call.data == "dolg_not_money": # Узнать долги/пересдать сессию
            first_str_8(call)
        elif call.data == "distance": # Заочка
            first_str_9(call)
        elif call.data == "practice": # Практика
            first_str_10(call)
        elif call.data == "afisha": # Афиша
            first_str_11(call)
        elif call.data == "clubs": # Клубы
            first_str_12(call)
        elif call.data == "dop_obrazov1": # Дополнительное образование или второй диплом
            first_str_13(call)
        elif call.data == "dop_obrazov2": # Дополнительное образование или второй диплом
            first_str_14(call)
        elif call.data == "study_plans": # Учебные планы
            first_str_15(call)
        elif call.data == "el_library": # Электронная библиотека
            first_str_16(call)
        elif call.data == "message_teacher": # Связаться с преподавателем
            first_str_17(call)
        elif call.data == "el_jur": # ЭлЖур
            first_str_18(call)
        elif call.data == "transport_card": # Транспортная карта
            first_str_19(call)
        elif call.data == "employers": # Сотрудники
            first_str_20(call)
        elif call.data == "psixolog": # Консультация психолога
            first_str_21(call)
        elif call.data == "self_control": # Самоконтроль
            first_str_22(call)
        elif call.data == "find_or_lost": # Потерял\нашел вещь
            first_str_23(call)
        elif call.data == "rules": # Правила внутреннего распорядка
            first_str_24(call)
        elif call.data == "kpp": # Пропускной режим
            first_str_25(call)
        elif call.data == "sales": # Скидки и виды поощрений
            first_str_26(call)
        elif call.data == "different_q": # Другой вопрос
            first_str_27(call)
        elif call.data == "links": # Ссылки
            first_str_28(call)



