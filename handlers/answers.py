from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.message(F.text.lower() == 'ответы на частые вопросы')
async def answers_handler(message: types.Message):
    await message.answer(
        text='Выберите тему, которая вас интересует:',
        reply_markup=create_category_of_answers_keyboard()
    )


@dp.callback_query(F.data.startswith('ans_'))
async def answers_handler_category(callback: types.CallbackQuery):
    session = create_session()
    text = 'Не удалось найти таких вопросов('
    id = callback.data.split("_")[-1]
    category = session.get(Categories, id).category
    if callback.data:
        text = f'Вопросы на тему "{category}":'
    await callback.message.answer(
        text=text,
        reply_markup=create_questions_keyboard(category=id)
    )


@dp.callback_query(F.data.startswith('quest_'))
async def questions_handler(callback: types.CallbackQuery):
    session = create_session()
    text = 'Не удалось найти ответов на такие вопросы('
    id = callback.data.split("_")[-1]
    question = session.get(Answers, id)
    if callback.data:
        text = question.answer
    await callback.message.answer(
        text=text
    )