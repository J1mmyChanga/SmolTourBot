from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.callback_query(F.data == 'recommendations')
async def recommendations_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text='Выберите, для какой категории вы бы хотели почитать рекомендации пользователей:',
        reply_markup=create_recommendations_keyboard()
    )


@dp.callback_query(F.data.startswith('rec_'))
async def recommendations_handler_category(callback: types.CallbackQuery):
    session = create_session()
    text = 'Не удалось найти таких рекомендаций('
    id = callback.data.split("_")[-1]
    category = session.get(Categories, id).category
    if callback.data:
        text = markdown.text(
            f'Пользовательские рекомендации на тему "{category}":',
            '',
            sep='\n'
        )
    await callback.message.answer(
        text=text,
    )