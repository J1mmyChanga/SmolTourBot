from aiogram import F
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.message(F.text.lower() == 'советы путешествующим')
async def advices_handler(message: types.Message):
    await message.answer(
        text='Советы от нас для тех, кто:',
        reply_markup=create_advices_keyboard()
    )


@dp.callback_query(F.data.startswith('ad_'))
async def advices_handler_param(callback: types.CallbackQuery):
    session = create_session()
    text = 'Не удалось найти таких мест('
    if callback.data:
        id = callback.data.split('_')[-1]
        param = session.get(AdviceParams, id).param
        text = f'Советы на тему "{param}":'
    await callback.message.answer(
        text=text,
    )