from aiogram import F
from create_entities import *
from misc import *


@dp.message(F.text.lower() == '❓ ответы на частые вопросы ❓')
async def answers_handler(message: types.Message):
    await message.answer(
        text='❓ Выберите тематику интересующего вас вопроса ❓:',
        reply_markup=create_category_of_answers_keyboard()
    )


@dp.callback_query(F.data.startswith('ans_'))
async def answers_handler_category(callback: types.CallbackQuery):
    session = create_session()
    id = callback.data.split("_")[-1]
    category = session.get(Categories, id).category
    text = f'❓ Многие туристы часто задаются вопросами на тему: "{category}" ❓:'
    await callback.message.answer(
        text=text,
        reply_markup=create_questions_keyboard(category=id)
    )


@dp.callback_query(F.data.startswith('quest_'))
async def questions_handler(callback: types.CallbackQuery):
    session = create_session()
    id = callback.data.split("_")[-1]
    question = session.get(Answers, id)
    text = question.answer
    await callback.message.answer(
        text=text
    )