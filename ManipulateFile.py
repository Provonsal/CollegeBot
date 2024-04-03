import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class ManipulateFile():
    def __init__(self, path: str, bot) -> None:
        self.path = path
        self.bot = bot

    def download_document(self, file_id: str):
        file_info = self.bot.get_file(file_id)
        downloaded_file = self.bot.download_file(file_info.file_path)
        
        with open(f'settings/settings_temp.json', 'wb') as new_file:
            new_file.write(downloaded_file)

    def delete_file(self):
        if os.path.isfile(self.path):
            os.remove(self.path)

    def rewrite_settings(default = 0):
        with open(f'settings/settings_temp.json', 'rb') as file:
            with open(f'settings/settings.json', 'wb') as new_file:
                new_file.write(file.read())

    def get_inline_buttons(default = 0) -> InlineKeyboardMarkup:
        reply: InlineKeyboardMarkup = InlineKeyboardMarkup(row_width=2)
        options: tuple = (
                        InlineKeyboardButton('Подтвердить', callback_data='confirm'),
                        InlineKeyboardButton('Отказать', callback_data='deny')
                        )
        reply.add(*options)
        return reply