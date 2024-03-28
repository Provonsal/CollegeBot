# coding=utf-8 

from typing import NoReturn
from SectionChooser import SectionChooser
from MenuCreator import MenuFromCall, MenuFromMessage
from tbot import bot, address, password, password2
from Info import Info
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os


def download_document(file_id: str):
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    
    with open(f'settings/settings_temp.json', 'wb') as new_file:
        new_file.write(downloaded_file)

def delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

def rewrite_settings():
    with open(f'settings/settings_temp.json', 'rb') as file:
        with open(f'settings/settings.json', 'wb') as new_file:
            new_file.write(file.read())

def get_inline_buttons() -> InlineKeyboardMarkup:
    reply: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
    options: tuple = (
                    InlineKeyboardButton('Подтвердить', callback_data='confirm'),
                    InlineKeyboardButton('Отказать', callback_data='deny')
                    )
    reply.add(*options)
    return reply

@bot.message_handler(commands=['start'])
def start(message) -> NoReturn:
    
    #bot.send_message(address, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    all_info = Info('aaa')
    menu = MenuFromMessage(bot, all_info, message, 1)
    menu.bot_menu_pager()

@bot.message_handler(content_types=['document'], func= lambda message: message.caption == password)
def change_settings(message) -> NoReturn:
    
    download_document(message.document.file_id)
    
    reply: InlineKeyboardMarkup = get_inline_buttons()

    bot.send_message(address,'Запрос на обновление файла настроек', reply_markup=reply)

@bot.message_handler(func= lambda message: message.text == password2)
def send_settings(message): 

    with open('settings/settings.json', 'rb') as file:
        bot.send_document(message.chat.id,file)

@bot.callback_query_handler(func=lambda call: call.data=="confirm")
def confirmation(call) -> NoReturn:

    rewrite_settings()

    delete_file("settings/settings_temp.json")

    bot.edit_message_text(
                        'Файл настроек успешно обновлен!',
                        call.message.chat.id,
                        call.message.message_id
                        )

@bot.callback_query_handler(func=lambda call: call.data=="deny")
def confirmation(call) -> NoReturn:

    delete_file("settings/settings_temp.json")

    bot.edit_message_text(
                        'Запрос на обновление файла настроек отклонен! Присланный файл стерт.',
                        call.message.chat.id,
                        call.message.message_id
                        )

@bot.callback_query_handler(func=lambda call: True)
def menu(call) -> NoReturn:
    
    call_data: str = call.data
    tmp = set(call_data)

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
