# coding=utf-8 

import telebot
from typing import NoReturn
from SectionChooser import SectionChooser
from MenuCreator import MenuFromCall, MenuFromMessage
from tbot import bot
from tbot import info




@bot.message_handler(commands=['start'])
def start(message) -> NoReturn:
    
    #bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    # markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    # button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='aab``1')
    # button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="aaE``1")
    # button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="aaZ``1")
    
    # markup.add(button_studRod, button_abitr, button_sotr, )
    
    # bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    all_info = info('aaa')
    menu = MenuFromMessage(bot, all_info, message, 1)
    menu.bot_menu_pager()
    
    

@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    call_data: str = call.data
    if '``' in call_data:
        wanted_page = (call_data.split('``'))[-1]
        call_data = (call_data.split('``'))[0]
    print(call_data)
    all_info = info(call_data)
    
    if all_info.buttons != None:
        menu = MenuFromCall(bot, call, all_info, wanted_page)
        menu.bot_menu_pager()
    else:
        section = SectionChooser(bot, call, all_info)
        section.section_selector()



bot.polling(none_stop=True)
