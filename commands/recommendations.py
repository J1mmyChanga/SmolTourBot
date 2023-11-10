from aiogram.filters import Command
from create_entities import *
from misc import *
@dp.message(Command('recommendations'))
async def recommendations_handler_command(message: types.Message):
    await message.answer(
        text='Выберите, для какой категории вы бы хотели почитать рекомендации пользователей:',
        reply_markup=create_recommendations_keyboard()
    )