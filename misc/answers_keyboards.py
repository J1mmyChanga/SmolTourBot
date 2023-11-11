from aiogram import types
from data import *


def create_category_of_answers_keyboard():
    session = create_session()
    categories = [(i.category, i.id) for i in session.query(Categories).all()]
    buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'ans_{i[1]}')] for i in categories]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard


def create_questions_keyboard(category):
    session = create_session()
    questions = [(i.question, i.id) for i in session.query(Answers).filter(Answers.category == category)]
    buttons = [[types.InlineKeyboardButton(text=i[0], callback_data=f'quest_{i[1]}')] for i in questions]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard