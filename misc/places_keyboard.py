from aiogram import types
from data import *


def create_places_keyboard():
    session = create_session()
    locations = [(i.location, i.id) for i in session.query(Locations).all()]
    buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'loc_{i[1]}')] for i in locations]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard