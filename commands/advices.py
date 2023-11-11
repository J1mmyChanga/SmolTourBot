from aiogram.filters import Command
from create_entities import *
from misc import *


@dp.message(Command('advices'))
async def advices_handler_command(message: types.Message):
    await message.answer(
        text='📒 Советы от нас для тех, кто 📒:',
        reply_markup=create_advices_keyboard()
    )
