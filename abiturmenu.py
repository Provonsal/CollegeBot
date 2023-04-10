# coding=utf-8 

import telebot
bot = telebot.TeleBot("6086891510:AAHhYBpEb_as4GwFW6Hw6N_y0yLcXDksW60")

class abitur():
    def abitur_bum(call):
        def first_str_1(call): # О колледже
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page1")
            button_2 = telebot.types.InlineKeyboardButton('Подробнее на сайте', url="https://opencollege-nsk.ru/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Новосибирский городской открытый колледж - это территория смыслов, личных возможностей и цифровых технологий.

Наша миссия - мы даём возможность каждому студенту стать главным участником учебного процесса, непринужденно и с интересом осваивать выбранную профессию, при этом жить активной студенческой жизнью и всесторонне развиваться. Личностно и профессионально.

Задача -  наш колледж готовит высококвалифицированных специалистов в соответствии с современными требованиями и с учетом интересов работодателей, способных выдержать конкуренцию на рынке труда.

Новосибирский городской открытый колледж входит в состав единого образовательного холдинга совместно с Московским экономическим институтом и Московским институтом психоанализа. Студентам колледжа доступен ряд льготных условий при поступлении в вузы-партнёры, включая зачисление без результатов ЕГЭ, скидку до 20% на оплату обучения, а также сокращенные сроки обучения в вузе.

Год основания: 2019
Количество студентов: 750+
Выпускников: 200+
Партнёры: 20+
Специальности: 13
Студенческие клубы: 20
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2(call): # Специальности
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page1")
            button_2 = telebot.types.InlineKeyboardButton('Дизайн (по отраслям)', callback_data="spec1")
            button_3 = telebot.types.InlineKeyboardButton('Реклама', callback_data="spec2")
            button_4 = telebot.types.InlineKeyboardButton('Информационные системы и программирование', callback_data="spec3")
            button_5 = telebot.types.InlineKeyboardButton('Юриспруденция', callback_data="spec4")
            button_6 = telebot.types.InlineKeyboardButton('Правоохранительная деятельность', callback_data="spec5")
            button_7 = telebot.types.InlineKeyboardButton('Операционная деятельность в логистике', callback_data="spec6")
            button_8 = telebot.types.InlineKeyboardButton('Экономика и бухгалтерский учет', callback_data="spec7")
            button_9 = telebot.types.InlineKeyboardButton('Коммерция', callback_data="spec8")
            button_10 = telebot.types.InlineKeyboardButton('Финансы', callback_data="spec9")
            button_11 = telebot.types.InlineKeyboardButton('Социально-культурная деятельность', callback_data="spec10")
            button_12 = telebot.types.InlineKeyboardButton('Народное художественное творчество', callback_data="spec11")
            button_13 = telebot.types.InlineKeyboardButton('Коррекционная педагогика в нач. образовании', callback_data="spec12")
            button_14 = telebot.types.InlineKeyboardButton('Специальное дошкольное образование', callback_data="spec13")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10,button_11,button_12,button_13, button_14,button_1, back)
            text = """Специальности:
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_1(call): # специальность дизайн
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            button_3 = telebot.types.InlineKeyboardButton('Видео про Дизайн', url="https://youtu.be/_1DTn-nMuAU")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_3,button_1, back)
            text = """Дизайн (по отраслям)

🎨 Дизайнер-это не художник, а скорее разработчик. Используя свою фантазию и навыки визуального оформления (это может быть рисование карандашом, проектирование на планшете или 3D-моделирование в специальной программе) он создает функциональную оболочку объекта или продукта.

👩‍💻 На специальности “Дизайн (по отраслям)” обучение осуществляется только по очной форме. Поступить на специальность можно после 9 и 11 класса.

📜 После окончания обучения Вы получите диплом государственного образца по квалификации - “Дизайнер”.

🖥 Узнать подробнее о специальности можно на нашем сайте: https://opencollege-nsk.ru/speciality/dizayn-po-otraslyam__298/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_2(call): # специальность реклама
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Реклама

📸 Любой организации, предоставляющей те или иные услуги, требуется специалист по рекламе. Специалист по рекламе отвечает за планирование и осуществление рекламных мероприятий по продвижению производимой организацией продукции или услуг и определяет затраты на их проведение с учетом характера спроса (равномерного или сезонного) на товары (услуги), совершенствует методы проведения рекламных мероприятий, эффективность и снижение затрат, связанных с рекламой. Кроме того, специалист по рекламе изучает данные анализа мотивации спроса на производимую продукцию или оказываемые услуги, действенности рекламы и определяет направленность проведения рекламных кампаний.

👩‍💻 На специальности “Реклама” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 и 11 класса.

📜 После окончания обучения Вы получите диплом государственного образца по квалификации - “Специалист по рекламе”.

🖥 Узнать подробнее о специальности можно на нашем сайте: https://opencollege-nsk.ru/speciality/reklama__297/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_3(call): # специальность инф системы и программ
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Информационные системы и программирование

⌨ На специальности “Информационные системы и программирование” обучение осуществляется только по очной форме. Поступить на специальность можно после 9 и 11 класса.

📜 После окончания обучения Вы получите диплом государственного образца по квалификации - “Специалист по информационным системам”.

🖥 Узнать подробнее о специальности можно на нашем сайте.

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_4(call): # специальность юриспруденция
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Юриспруденция 

👨‍⚖Образовательная программа направлена на подготовку юристов среднего звена в сфере обеспечения реализации прав граждан в сфере пенсионного обеспечения и социальной защиты, а также организационного обеспечения деятельности учреждений социальной защиты населения и органов Пенсионного фонда Российской Федерации.

👩‍💻На специальности “Юриспруденция” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Юрист”.

🖥Узнать подробнее о специальности можно на нашем сайте
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_5(call): # специальность правоохрана
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Правоохранительная деятельность

⏳На специальности “Правоохранительная деятельность” обучение осуществляется по очной и очно-заочной форме. Поступить на специальность можно после 9 (очная форма) и 11 класса (очно-заочная форма).

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Юрист”.

🖥Узнать подробнее о специальности можно на нашем сайте.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_6(call): # специальность логистика
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Операционная деятельность в логистике

🚛 Логист – это человек, который профессионально занимается доставкой товара, дальнейшим его складированием, а также тот, кто разрабатывает наиболее выгодную схему поставок. Это человек, который ищет надежных партнеров, проводит расчеты, занимается анализом рынка транспортных услуг, готовит необходимые документы.

👩‍💻На специальности “Операционная деятельность в логистике” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Операционный логист”.

🖥Узнать подробнее о специальности можно на нашем сайте: https://opencollege-nsk.ru/speciality/operatsionnaya-deyatelnost-v-logistike__293/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_7(call): # специальность бухг учет
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Экономика и бухгалтерский учет

💰 Бухгалтерия – одно из самых популярных направлений среди специальностей среднего профессионального образования. Глубокие теоретические знания и практическая отработка навыков по ведению бухгалтерского учета предприятия – этой подготовки достаточно для квалифицированного и грамотного обеспечения финансовой стабильности предприятия.

👩‍💻На специальности “Экономика и бухгалтерский учет (по отраслям)” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Бухгалтер”.

🖥Узнать подробнее о специальности можно на нашем сайте: https://opencollege-nsk.ru/speciality/ekonomika-i-bukhgalterskiy-uchet__292/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_8(call): # специальность коммерция
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Коммерция

🛍 Вы сделаете выгодную и долгосрочную инвестицию в свое стабильное и успешное будущее. Вы станете востребованным специалистом на рынке труда, так как у вас будет достаточно знаний и навыков, которые ценятся в каждой компании. Таких навыков, которых, при желании, будет достаточно даже для открытия своего собственного бизнеса.

👩‍💻На специальности “Коммерция (по отраслям)” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Менеджер по продажам”.

🖥Узнать подробнее о специальности можно на нашем сайте: https://opencollege-nsk.ru/speciality/kommertsiya-po-otraslyam__295/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_9(call): # специальность финансы
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Финансы

💴 В условиях рыночной экономики финансовая стабильность компании является основой ее развития. Менеджмент предприятия направляет усилия на обеспечение финансового роста, увеличение прибылей, улучшение всех экономических показателей. Поэтому в штатной структуре фирмы весомую роль играют финансисты, отвечающие за ее финансово-кредитную политику. С учетом важности этого направления в бизнесе специалисты имеющие квалификацию финансиста пользуются большим спросом.

👩‍💻На специальности “Финансы” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации -”Финансист”.

🖥Узнать подробнее о специальности можно на нашем сайте: https://opencollege-nsk.ru/speciality/kommertsiya-po-otraslyam__295/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_10(call): # специальность соц-культурная деятельность
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Социально-культурная деятельность

🎭На специальности “Социально-культурная деятельность (по видам) ” обучение осуществляется только по очной форме. Поступить на специальность можно после 9 и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Менеджер социально-культурной деятельности” и сертификат установленного образца Event-менеджера.

🖥Узнать подробнее о специальности можно на нашем сайте.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_11(call): # специальность народное худ творчество
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Народное художественное творчество

💃На специальности “Народное художественное творчество (по видам) ” обучение осуществляется только по очной форме. Поступить на специальность можно после 9 класса.

📜После окончания обучения Вы получите диплом государственного образца по квалификации - “Руководитель любительского творческого коллектива, преподаватель”.

🖥Узнать подробнее о специальности можно на нашем сайте.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_12(call): # специальность коррекционная педагогика
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Коррекционная педагогика в начальном образовании

👩‍🏫На специальности “Коррекционная педагогика в начальном образовании” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 класса и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по профессии - “Учитель начальных классов и начальных классов компенсирующего и коррекционно-развивающего образования”.

🖥Узнать подробнее о специальности можно на нашем сайте.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_2_13(call): # специальность спец дошкольное образование
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="specials")
            button_2 = telebot.types.InlineKeyboardButton('На сайт', url="https://opencollege-nsk.ru/speciality/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Специальное дошкольное образование

👩‍🏫На специальности “Специальное дошкольное образование” обучение осуществляется по очной и заочной форме. Поступить на специальность можно после 9 класса и 11 класса.

📜После окончания обучения Вы получите диплом государственного образца по профессии - “Воспитатель детей дошкольного возраста с отклонениями в развитии и с сохранным развитием”.

🖥Узнать подробнее о специальности можно на нашем сайте.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_3(call): # Документы для поступления
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page1")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Для поступления Вам потребуется минимальный пакет документов (обязательно при подаче документов на любую форму обучения):

1️⃣ - документ, удостоверяющий личность, гражданство (страница с паспортными данными + страница с регистрацией);

2️⃣ - документ, удостоверяющий личность законного представителя (страницы с паспортными данными + страница с регистрацией);

3️⃣ - документ об образовании установленного образца;

4️⃣ - СНИЛС;

5️⃣ - 4 фотографии размером 3*4 (цветной снимок на матовой бумаге, сделанный в текущем году);

6️⃣ - документ, подтверждающий наличие льгот для предоставления скидок на обучение (при необходимости).

Дополнительно (обязательно на 01.09 для обучения на очной и очно-заочной форме):

7️⃣ - медицинская справка, форма 086-У для всех специальностей очной и очно-заочной формы (оригинал)

8️⃣- страховой медицинский полис (копия)

9️⃣ - приписное/военный билет (для юношей);

🔟 - документы о смене фамилии/имени/отчества (при необходимости).

▶️ Дополнительно для лиц с инвалидностью и ОВЗ:

документ, подтверждающий инвалидность или ОВЗ, требующие создания специальных условий обучения.

🔤 Дополнительно для иностранных граждан:

нотариально заверенный перевод документов.

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_4(call): # Как поступить
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page1")
            button_2 = telebot.types.InlineKeyboardButton('Записаться на прием', url="https://opencollege-nsk.ru/enrollee/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Документы для поступления можно подать следующими способами:

1️⃣ - лично по предварительной записи на сайте - https://opencollege-nsk.ru/enrollee/

2️⃣ - курьерской службой по адресу – г. Новосибирск, ул. 2-я Союза Молодёжи, д. 31

ДЛЯ ПОДАЧИ ДОКУМЕНТОВ ЛИЧНО В ПРИЕМНОЙ КОМИССИИ НЕОБХОДИМА ПРЕДВАРИТЕЛЬНАЯ ЗАПИСЬ

🗺 Адрес: 
630082, Россия, г. Новосибирск, ул.2-я Союза Молодежи д.31 каб.271

📅 График работы: 
понедельник-пятница

⏰ Часы работы: 
с 9.00 до 19.00

☎️ Телефон: 
+7 (383) 363-63-63, 
+7 (913) 207-98-20, 
+7 (913) 207-93-60

📬 E-mail: 
priem@opencollege-nsk.ru

Ответственный секретарь приемной комиссии: 
Коробкина Марина Александровна

Специалист отдела по работе с абитуриентами: 
Криничная Елена Владимировна

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_5(call): # Стоимость обучения и скидки
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page1")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/enrollee/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Стоимость обучения зависит от формы обучения и специальности которую Вы выбираете. Размер скидки зависит от различных факторов (балла аттестата, портфолио, социальных льгот и другого).

Подробнее ознакомиться со стоимостью обучения и скидками можно на нашем сайте: https://opencollege-nsk.ru/enrollee/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_6(call): # Вступительные испытания
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page2")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/enrollee/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Для некоторых наших направлений подготовки предусмотрены вступительные испытания. Как правило, это те направления, которые требуют определенных навыков (дизайн, реклама, народное художественное творчество). 

На нашем сайте представлен список таких специальностей, а также видов и сроков проведения вступительных испытаний. 

На сайте Вы можете самостоятельно записаться на вступительное испытание.
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_7(call): # Дополнительное образование
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page2")
            button_2 = telebot.types.InlineKeyboardButton('“Перейти на сайт', url="https://opencollege-nsk.ru/education/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Ты хочешь развиваться сразу в нескольких направлениях и успеть за студенческие годы как можно больше?

А может, тебе кажется, что ты поступил не совсем туда, и осознание этого пришло уже во время учебы.

Бросать и начинать все заново не хочется – и в этом нет необходимости: ты можешь найти желаемую специализацию в списке программ дополнительного профессионального образования и заниматься параллельно.

Узнать подробнее и записаться на обучение по программам дополнительного образования можно в отделе дополнительного образования (каб.263) у руководителя направления - Суминой Юлии Александровны с ПН по ПТ с 9:00 до 18:00, или телефону: 8 (905)-934-73-33, а также 8 (383) 363-63-63, добавочный 1012.

E-mail: do@opencollege-nsk.ru или в ТГ: @ngok_do

Подробнее о программах ДО можно узнать на нашем сайте https://opencollege-nsk.ru/education/

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_8(call): # Внеучебные траектории
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page2")
            button_2 = telebot.types.InlineKeyboardButton('Узнать подробнее', url="https://opencollege-nsk.ru/live/extracurricular/?group=creation")
            button_3 = telebot.types.InlineKeyboardButton('Студенчкский совет', url="https://opencollege-nsk.ru/live/association/")
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
        def first_str_9(call): # Лицензия и аккредитация
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page2")
            button_2 = telebot.types.InlineKeyboardButton('“Перейти на сайт', url="https://opencollege-nsk.ru/college/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """АНО СПО “НГОК” имеет лицензию на образовательную деятельность и государственную аккредитацию, что дает право колледжу осуществлять набор студентов и выдавать дипломы государственного образца. 

Наши студенты имеют право на пользование муниципальными льготами и право на отсрочку от службы в армии.

Посмотреть документы (лицензию и свидетельства об аккредитации) можно на нашем сайте по ссылке: https://opencollege-nsk.ru/college/
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_10(call): # Партнеры колледжа
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page2")
            button_2 = telebot.types.InlineKeyboardButton('Перейти на сайт', url="https://opencollege-nsk.ru/college/partners/")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Наш колледж входит в большой образовательный холдинг, но помимо наших образовательных учреждений, мы дружим с другими организациями в сфере образования, науки, бизнеса, культуры, социальной политики, медицины и других сфер. 

Узнать подробнее о наших партнеров можно на сайте - https://opencollege-nsk.ru/college/partners/

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_11(call): # Афиша мероприятий
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page3")
            button_2 = telebot.types.InlineKeyboardButton('Перейти в канал', url="https://t.me/pencollege2023")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """Для гостей и абитуриентов колледжа мы проводим различные мероприятия: дни открытых дверей, мастер-классы, лекции, школы дополнительного образования, курсы подготовки к экзаменам. Большинство из этих мероприятий являются бесплатными.

Подробнее узнать и посмотреть список мероприятий можно в телеграм-канале Абитуриентов колледжа @opencollege2023
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_12(call): # Кураторы и наставники
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page3")
            button_2 = telebot.types.InlineKeyboardButton('Список кураторов и наставников', url="https://docs.google.com/spreadsheets/d/1b6Lz7k3KT8uDlekmWQZ30HxZ_5jeEll3ERz5uw4bs4M/edit?usp=drivesdk")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_2,button_1, back)
            text = """В нашем колледже за каждой группой закреплен сотрудник - куратор учебной группы. 

Кураторы группы - это самые активные, коммуникабельные и творческие наши сотрудники. 

Кураторы помогают нашим студентам адаптироваться к образовательному процессу, разрешают сложные ситуации в учебной деятельности, помогают найти контакт студентам между собой и с преподавателями, контролируют поведение студентов, посещаемость и успеваемость (при необходимости проводят беседы со студентом, а если это ее помогает, то с родителями). 

Кураторы проводят культурные мероприятия, такие как: чаепития, экскурсии, квартирники, вечера настольных игр и другие.

Вместе с кураторами, у первокурсников есть Наставники. Наставники - это активные студенты старших курсов, которые хотят поделиться своими знаниями и опытом с первокурсниками. 

Наставники помогут Вам адаптироваться в колледже, расскажут подробнее о том, как проходит учебный и внеучебный процесс со своего студенческого взгляда.

Практически все наставники состоят во внеучебных траекториях и студенческих клубах, они подробно расскажут Вам о них и помогут вступить в активную студенческую жизнь! 

Кураторы и наставники встретят Вас 1 сентября, проведут экскурсию и познакомят друг с другом. Те группы, которые сформируются раньше, смогут увидеться со своим наставником в августе, возможно сходить на пикник или другое мероприятие.

Для всех групп первого курса будут созданы коммуникационные чаты по направлениям, где вы все сможете познакомиться между собой. 

Ссылки на чаты появятся в этом разделе в конце августа.

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_13(call): # Как добраться?
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page3")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """АНО СПО “НГОК” находится по адресу: г. Новосибирск, ул. 2-я Союза Молодежи, дом 31 (вход в правое крыло здания).

Добраться до колледжа можно на общественном транспорте: 

1️⃣ - на метро (до станции метро “Заельцовская и пройти пешком 1 км за 7-15 минут);

2️⃣ - на автобусе № 14, 34, 64, 75, 95 (до остановки “Плановая” или “Магазин Уют” и пройти пешком 300 - 400 метров за 1-3 минуты); 

3️⃣ - на троллейбусе №2, 24 (до остановки “Плановая” или “Магазин Уют” и пройти пешком 300 - 400 метров за 1-3 минуты);

4️⃣ - на маршрутке №9, 11, 19, 25, 28, 30, 30а, 34, 45, 53, 73, 87 (до остановки “Плановая” или “Магазин Уют” и пройти пешком 300 - 400 метров за 1-3 минуты);

А также добраться можно на собственном транспорте, такси или пешком (если проживаете рядом с колледжем).

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_14(call): # Оплатить обучение
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page3")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Оплатить обучение можно онлайн! 

График платежей у каждого индивидуальный, посмотреть его можно в приложении к Вашему договору, но если Вы не помните свой график, можно уточнить его в приемной комиссии по телефону 8 (383) 363-63-63, доб.1014. 

ИНСТРУКЦИЯ ПО ОПЛАТЕ ЧЕРЕЗ ПРИЛОЖЕНИЕ СБЕРА (можно оплатить через другое)

1️⃣ - Вкладка «Платежи»

2️⃣ - В поисковой строке выбираете «Платеж по реквизитам»

3️⃣ - Выбираете «Оплата по ИНН» и вводите наш ИНН 5404089162

4️⃣ - Заполняете поля «Расчетный счет получателя» и «БИК банка получателя»
Р/с 40703810744050003777
БИК 045004641

5️⃣ - В следующей вкладке вы увидите наше наименование АНО СПО "НОВОСИБИРСКИЙ ГОРОДСКОЙ ОТКРЫТЫЙ КОЛЛЕДЖ" - это подтверждение того, что все данные заполнены верно. 

6️⃣ - Заполняете ФИО плательщика (ФИО обучающегося или родителя, указанного в договоре) и назначение платежа «Оплата за обучение студента ФИО, № договора»

7️⃣ - Вводите сумму

8️⃣ - Производите оплату

"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
        def first_str_15(call): # Наш сайт и социальные сети
            global bot
            next_menu = telebot.types.InlineKeyboardMarkup(row_width=1)
            button_1 = telebot.types.InlineKeyboardButton('🔙 Назад 🔙', callback_data="Abitur_page3")
            back = telebot.types.InlineKeyboardButton(text='📱 В меню 📱', callback_data='mainmenu')
            next_menu.add(button_1, back)
            text = """Наш сайт: https://opencollege-nsk.ru/

Телеграм канал: t.me/opencollege_nsk

ВКонтакте: https://vk.com/opencollege_nsk

Инстаграм: https://instagram.com/opencollege.nsk

YouTube: https://youtube.com/@opencollege54

Телеграм канал Внеучебной жизни: t.me/vd_ngok

Телеграм канал для Абитуриентов: t.me/opencollege2023


Телеграм канал Центра карьеры и практики: t.me/praktika_ngok

Чат иногородних студентов: t.me/unified_college

ЭлЖур: https://opencollege-nsk.eljur.ru/authorize

* Instagram, продукт компании Meta, которая признана экстремистской организацией в России
"""
            bot.edit_message_text(text, call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)    
    
        if call.data == "about": # О колледже
            return first_str_1(call)
        elif call.data == "specials": # Специальности
            return first_str_2(call)
        elif call.data == "spec1": # Специальность дизайн
            return first_str_2_1(call)
        elif call.data == "spec2": # Специальности реклама
            return first_str_2_2(call)
        elif call.data == "spec3": # Специальности инф системы и программ
            return first_str_2_3(call)
        elif call.data == "spec4": # Специальности юриспруденция
            return first_str_2_4(call)
        elif call.data == "spec5": # Специальности правоохран деят
            return first_str_2_5(call)
        elif call.data == "spec6": # Специальности операционная деятельность в логистике
            return first_str_2_6(call)
        elif call.data == "spec7": # Специальности экономика и бухг учет
            return first_str_2_7(call)
        elif call.data == "spec8": # Специальности коммерция
            return first_str_2_8(call)
        elif call.data == "spec9": # Специальности финансы
            return first_str_2_9(call)
        elif call.data == "spec10": # Специальности соц-культ деятельность
            return first_str_2_10(call)
        elif call.data == "spec11": # Специальности народное худ творчество
            return first_str_2_11(call)
        elif call.data == "spec12": # Специальности коррекцияонная педагогика в нач образовании
            return first_str_2_12(call)
        elif call.data == "spec13": # Специальности Специальное дошкольное образование
            return first_str_2_13(call)
        elif call.data == "docum": # документы
            return first_str_3(call)
        elif call.data == "kak_postup": # как поступить
            return first_str_4(call)
        elif call.data == "cost": # цена обучения
            return first_str_5(call)
        elif call.data == "exams": # Вступительные испытания
            return first_str_6(call)
        elif call.data == "dop_degree": # доп образование
            return first_str_7(call)
        elif call.data == "clubs_abitur": # клубы
            return first_str_8(call)
        elif call.data == "license1": # Лицензия и аккредитация
            return first_str_9(call)
        elif call.data == "partnership": # Партнеры колледжа
            return first_str_10(call)
        elif call.data == "affisha": # афиша
            return first_str_11(call)
        elif call.data == "kuratori": # кураторы
            return first_str_12(call)
        elif call.data == "way": # как добраться
            return first_str_13(call)
        elif call.data == "transac": # оплата
            return first_str_14(call)
        elif call.data == "links1": # ссылки
            return first_str_15(call)


