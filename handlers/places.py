from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.callback_query(F.data == 'places')
async def places_handler(callback: types.CallbackQuery):
    await callback.message.answer(
        text='Выберите локацию, в которой хотели бы сфотографироваться',
        reply_markup=create_places_keyboard()
    )


@dp.callback_query(F.data.startswith('loc_'))
async def places_handler_location(callback: types.CallbackQuery):
    text = 'Не удалось найти таких мест('
    if callback.data == 'loc_parks':
        text = markdown.text(
            'Вот красивые локации для фото в парках:',
            '',
            sep='\n'
        )
    elif callback.data == 'loc_history':
        text = markdown.text(
            'Вот красивые локации для фото в исторических местах:',
            '',
            sep='\n'
        )
    elif callback.data == 'loc_architecture':
        text = markdown.text(
            'Вот красивые локации для местах с красивой архитектурой:',
            '',
            sep='\n'
        )
    await callback.message.answer(
        text=text,
    )