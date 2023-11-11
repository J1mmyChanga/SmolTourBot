from aiogram import types

def create_func_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='Места для фотосессий', callback_data='places')],
        [types.InlineKeyboardButton(text='Советы путешествующим', callback_data='advices')],
        [types.InlineKeyboardButton(text='Рекомендации от пользователей', callback_data='recommendations')],
        [types.InlineKeyboardButton(text='Ответы на частые вопросы', callback_data='answers')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard