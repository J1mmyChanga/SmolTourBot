from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.callback_query(F.data == 'advices')
async def advices_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text='Советы от нас для тех, кто:',
        reply_markup=create_advices_keyboard()
    )


@dp.message(Command('advices'))
async def advices_handler(message: types.Message):
    await message.answer(
        text='Советы от нас для тех, кто:',
        reply_markup=create_advices_keyboard()
    )


@dp.callback_query(F.data.startswith('ad_'))
async def advices_handler_param(callback: types.CallbackQuery):
    text = 'Не удалось найти таких мест('
    if callback.data == 'ad_family':
        text = markdown.text(
            'Если вы путешествуете всей семьёй, то вы можете:',
            '',
            sep='\n'
        )
    elif callback.data == 'ad_food':
        text = markdown.text(
            'Вы хотите хорошо покушать? Тогда почему бы не:',
            '',
            sep='\n'
        )
    elif callback.data == 'ad_entertainment':
        text = markdown.text(
            'Хочется развлечься? Тогда вы можете:',
            '',
            sep='\n'
        )
    await callback.message.answer(
        text=text,
    )