# coding=utf-8 

from typing import NoReturn
from SectionChooser import SectionChooser
from MenuCreator import MenuFromCall, MenuFromMessage
from tbot import bot
from tbot import Info




@bot.message_handler(commands=['start'])
def start(message) -> NoReturn:
    
    #bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    all_info = Info('aaa')
    menu = MenuFromMessage(bot, all_info, message, 1)
    menu.bot_menu_pager()
    
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
