from aiogram import types
from data import *


def create_recommendations_keyboard():
    session = create_session()
    categories = [(i.category, i.id) for i in session.query(Categories).all()]
    buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'rec_{i[1]}')] for i in categories]
    buttons.append([types.InlineKeyboardButton(text='Добавить рекомендацию', callback_data=f'custom_recommendation')])
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def create_recommendations_to_categories_keyboard():
    session = create_session()
    categories = [(i.category, i.id) for i in session.query(Categories).all()]
    buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'add_rec_{i[1]}')] for i in categories]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard