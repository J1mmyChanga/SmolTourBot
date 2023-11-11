from aiogram import types
from data import *


def create_advices_keyboard():
    session = create_session()
    params = [(i.param, i.id) for i in session.query(AdviceParams).all()]
    buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'ad_{i[1]}')] for i in params]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
