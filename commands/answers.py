from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.message(Command('answers'))
async def answers_handler_command(message: types.Message):
    await message.answer(
        text='Выберите тему, которая вас интересует:',
        reply_markup=create_categrory_of_answers_keyboard()
    )