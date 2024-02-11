# coding=utf-8 


from studmenpages import Menu
from tbot import bot, page_names
from tbot import current_time
import telebot



@bot.message_handler(commands=['start'])
def start(message):
    
    bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Стартанул Бота (написал /start)'.format(current_time(), message.from_user.id, message.from_user.first_name, message.from_user.last_name, message.from_user.username))
    
    markup = telebot.types.InlineKeyboardMarkup(row_width = 1)
    
    button_studRod = telebot.types.InlineKeyboardButton(text='Студент/Родитель', callback_data='Stud_page1')
    button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник/Преподаватель', callback_data="Sotr_page1")
    button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент/Родитель абитуриента', callback_data="Abitur_page1")
    
    markup.add(button_studRod, button_abitr, button_sotr, )
    
    bot.send_message(message.chat.id, 'Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?', reply_markup = markup)
    
    
    
@bot.callback_query_handler(func=lambda call: True)
def menu(call):
    
    if call.data == 'mainmenu': # Главное меню
        
        bot.send_message(-1001822755040, '{} \n<{}> <{}> <{}> <{}>\n\n Вернулся в Главное меню'.format(current_time(), call.from_user.id, call.from_user.first_name, call.from_user.last_name,call.from_user.username))
        
        mainmenu = telebot.types.InlineKeyboardMarkup(row_width = 1)
        
        button_studRod = telebot.types.InlineKeyboardButton(text='Студент\Родитель', callback_data='Stud_page1')
        button_sotr = telebot.types.InlineKeyboardButton(text='Сотрудник\Преподаватель', callback_data='Sotr_page1')
        button_abitr = telebot.types.InlineKeyboardButton(text='Абитуриент\Родитель абитуриента', callback_data='Abitur_page1')
        
        mainmenu.add(button_studRod, button_abitr,button_sotr)
        
        bot.edit_message_text("Приветствую Вас! Я бот Новосибирского городского открытого колледжа, подскажите, а кем являетесь Вы?", call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
        
    if '_page' in call.data:
        menuг = Menu(bot, call, page_names[call.data[:-6]], call.data)
        print(call.data)    
        menuг.bot_menu_pager(int(call.data[-1]))
    elif 'Stud_' in call.data:
        pass
    elif 'Sotr_' in call.data:
        pass
    else:
        pass


bot.polling(none_stop=True)
