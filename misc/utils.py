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


def create_places_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='Парки', callback_data='loc_parks')],
        [types.InlineKeyboardButton(text='Исторические места', callback_data='loc_history')],
        [types.InlineKeyboardButton(text='Интересная архитектура', callback_data='loc_architecture')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def create_advices_keyboard():
    buttons = [
        [types.InlineKeyboardButton(text='Путешествует всей семьёй', callback_data='ad_family')],
        [types.InlineKeyboardButton(text='Хочет вкусно покушать', callback_data='ad_food')],
        [types.InlineKeyboardButton(text='Ищет интересные развлечения', callback_data='ad_entertainment')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard