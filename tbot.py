# coding=utf-8 
from datetime import datetime, timedelta
import telebot

bot = telebot.TeleBot("6269939624:AAGAv4FO_FD5JvfRlSSWPiednZXPesUbZhU")

def current_time():
    now = datetime.now() + timedelta(hours=4)
    current_time = now.strftime("%H:%M:%S")
    return current_time


page_names = {
              'Stud': (
                        ( # callbacks
                            "spravka",
                            "otsrochka",
                            "rasp zanyat",
                            "rasp zvon",
                            "message_admin",
                            "oplata",
                            "dolg_money",
                            "dolg_not_money",
                            "distance",
                            "practice",
                            "afisha",
                            "clubs",
                            "dop_obrazov1",
                            "dop_obrazov2",
                            "study_plans",
                            "el_library",
                            "message_teacher",
                            "el_jur",
                            "transport_card",
                            "employee",
                            "psixolog",
                            "self_control",
                            "find_or_lost",
                            "rules",
                            "kpp",
                            "sales",
                            "different_q",
                            "links"
                        ),
                        ( # текст для кнопок
                            'Получить справку',
                            'Отсрочка от армии',
                            'Расписание занятий',
                            'Расписание звонков',
                            'Оплатить обучение',
                            'Узнать задолженность (финансовую)',
                            'Узнать долги/пересдать сессию',
                            'Заочное обучение',
                            'Практика',
                            'Афиша мероприятий',
                            'Внеучебные траектории и клубы',
                            'Дополнительное образование',
                            'Второй диплом',
                            'Учебные планы',
                            'Электронная библиотека',
                            'Связаться с преподавателем',
                            'Доступ в ЭлЖур',
                            'Транспортная карта',
                            'Список сотрудников',
                            'Консультация психолога',
                            'Самоуправление',
                            'Потерял/нашел вещь',
                            'Правила внутреннего распорядка',
                            'Пропускной режим',
                            'Скидки и виды поощрений',
                            'Другой вопрос',
                            'Связаться с администрацией',
                            'Наш сайт и социальные сети'
                        )
                    ),
              'Sotr': (
                        ( # callbacks
                            'raspis_zanyat',
                            'raspis_zvonkov',
                            'events',
                            'dopolnitel_obr',
                            'vedomost',
                            'dostupElJur',
                            'Tech_diff',
                            'post',
                            'kuratoru',
                            'plans',
                            'electr_lib',
                            'message_student',
                            'student_diff',
                            'trud',
                            'propusk',
                            'rekvisit',
                            'other_question',
                            'links_sotr'

                        ),
                        (   # текст кнопок
                            'Расписание занятий',
                            'Расписание звонков',
                            'Мероприятия',
                            'Дополнительное образование',
                            'Получить ведомость',
                            'Доступ в ЭлЖур',
                            'Технические сложности',
                            'Опубликовать пост',
                            'Куратору групп',
                            'Учебные планы',
                            'Электронная библиотека',
                            'Связаться со студентом',
                            'Сложности со студентами',
                            'Трудоустройство/оплата',
                            'Пропускной режим',
                            'Реквизиты колледжа',
                            'Другой вопрос',
                            'Наш сайт и социальные сети'
                        )
                    ),
              'Abitur': (
                            ( # callbacks
                                'about',
                                'specials',
                                'docum',
                                'kak_postup',
                                'cost',
                                'exams',
                                'dop_degree',
                                'clubs_abitur',
                                'license1',
                                'partnership',
                                'affisha',
                                'kuratori',
                                'way',
                                'transac',
                                'links1',
                                'spec1',
                                'spec2',
                                'spec3',
                                'spec4',
                                'spec5',
                                'spec6',
                                'spec7',
                                'spec8',
                                'spec9',
                                'spec10',
                                'spec11',
                                'spec12',
                                'spec13',
                            ),
                            (
                                'О колледже',
                                'Специальности',
                                'Документы для поступления',
                                'Как поступить?',
                                'Стоимость обучения и скидки',
                                'Вступительные испытания',
                                'Дополнительное образование',
                                'Внеучебные траектории и клубы',
                                'Лицензия и аккредитация',
                                'Партнеры колледжа',
                                'Афиша мероприятий',
                                'Кураторы и наставники',
                                'Как добраться?',
                                'Оплатить обучение',
                                'Наш сайт и социальные сети'
                            )
                    )}

