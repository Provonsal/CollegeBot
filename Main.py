# coding=utf-8 

import os
from typing import NoReturn
from SectionChooser import SectionChooser
from MenuCreator import MenuFromCall, MenuFromMessage
from ManipulateFile import ManipulateFile
from tbot import bot, address, password, password2
from Info import Info
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from tbot import bot, address, password, password2


@bot.message_handler(commands=['start'])
def start(message) -> NoReturn:
    
    #bot.send_message(address, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    all_info = Info('aaa')
    menu = MenuFromMessage(bot, all_info, message, 1)
    menu.bot_menu_pager()

@bot.message_handler(content_types=['document'], func= lambda message: message.caption == password)
def change_settings(message) -> NoReturn:
    
    manfile = ManipulateFile("settings/settings_temp.json", bot)

    manfile.download_document(message.document.file_id)
    
    reply: InlineKeyboardMarkup = manfile.get_inline_buttons()

    bot.send_message(address,'Запрос на обновление файла настроек', reply_markup=reply)

@bot.message_handler(func= lambda message: message.text == password2)
def send_settings(message): 
    if os.path.isfile('~/settings/settings.json'):
        with open('~/settings/settings.json', 'rb') as file:
            bot.send_document(message.chat.id,file)

@bot.callback_query_handler(func=lambda call: call.data=="confirm")
def confirmation(call) -> NoReturn:

    manfile = ManipulateFile("settings/settings_temp.json", bot)

    manfile.rewrite_settings()

    manfile.delete_file()

    bot.edit_message_text(
                        'Файл настроек успешно обновлен!',
                        call.message.chat.id,
                        call.message.message_id
                        )

@bot.callback_query_handler(func=lambda call: call.data=="deny")
def confirmation(call) -> NoReturn:

    manfile = ManipulateFile("settings/settings_temp.json", bot)

    manfile.delete_file()

    bot.edit_message_text(
                        'Запрос на обновление файла настроек отклонен! Присланный файл стерт.',
                        call.message.chat.id,
                        call.message.message_id
                        )

@bot.callback_query_handler(func=lambda call: True)
def menu(call) -> NoReturn:
    
    call_data: str = call.data
    tmp = set(call_data)

    bot.send_message(address, f'{current_time()} \n<{call.from_user.id}> <{call.from_user.first_name}> <{call.from_user.last_name}> <{call.from_user.username}>\n\n зашел в меню {call_data}')

    if call_data == 'None': return
    
    elif '`' in tmp: call_data, wanted_page = call_data.split('``')
    
    all_info = Info(call_data)
    
    if all_info.buttons != None:
        menublabla = MenuFromCall(bot, call, all_info, wanted_page)
        menublabla.bot_menu_pager()
        
    else:
        section = SectionChooser(bot, call, all_info)
        section.section_selector()
        
if __name__ == '__main__':
    bot.polling(none_stop=True)
