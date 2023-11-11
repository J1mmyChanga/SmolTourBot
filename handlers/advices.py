from aiogram import F
from create_entities import *
from misc import *


@dp.message(F.text.lower() == '📒 советы путешественникам 📒')
async def advices_handler(message: types.Message):
    await message.answer(
        text='📒 Если вы в чем то сомневаетесь, то всегда можете воспользоваться нашими советами: 📒:',
        reply_markup=create_advices_keyboard()
    )


@dp.callback_query(F.data.startswith('ad_'))
async def advices_handler_param(callback: types.CallbackQuery):
    session = create_session()
    id = callback.data.split('_')[-1]
    param = session.get(AdviceParams, id).param
    advices = [i.advice for i in session.query(Advices).filter(Advices.param == id)]
    await callback.message.answer(f'📒 На тему: "{param}" мы предлагаем такие советы 📒:')
    for i in advices:
        await callback.message.answer(f'📝 {i}')