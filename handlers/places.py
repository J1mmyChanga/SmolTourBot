from aiogram import types, F
from aiogram.filters import Command
from aiogram.utils import markdown
from create_entities import *
from misc import *


@dp.message(F.text.lower() == 'места для фотосессий')
async def places_handler(message: types.Message):
    await message.answer(
        text='Выберите локацию, в которой хотели бы сфотографироваться',
        reply_markup=create_places_keyboard()
    )


@dp.callback_query(F.data.startswith('loc_'))
async def places_handler_location(callback: types.CallbackQuery):
    text = 'Не удалось найти таких мест('
    if callback.data:
        id = callback.data.split('_')[-1]
        location = session.get(Locations, id).location
        places = [i.address for i in session.query(Places).filter(Places.location == location)]
        await callback.message.answer(f'Лучшие места в локации "{location}":')
        for i in places:
            latitude, longitude = get_coords(i)
            await callback.message.answer(i)
            await bot.send_location(callback.from_user.id, longitude, latitude)