from aiogram.filters import Command
from create_entities import *
from misc import *


@dp.message(Command('places'))
async def places_handler_command(message: types.Message):
    await message.answer(
        text='Выберите локацию, в которой хотели бы сфотографироваться',
        reply_markup=create_places_keyboard()
    )