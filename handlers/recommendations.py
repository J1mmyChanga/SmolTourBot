from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils import markdown
from create_entities import *
from misc import *


class RecommendationState(StatesGroup):
    recommendation = State()
    category = State()


@dp.message(F.text.lower() == '✉ рекомендации от пользователей ✉')
async def recommendations_handler(message: types.Message):
    await message.answer(
        text='📝 Выберите, для какой категории вы бы хотели почитать рекомендации пользователей: 📝',
        reply_markup=create_recommendations_keyboard()
    )


@dp.callback_query(F.data.startswith('rec_'))
async def recommendations_handler_category(callback: types.CallbackQuery):
    session = create_session()
    id = callback.data.split("_")[-1]
    category = session.get(Categories, id).category
    recommendations = [i.recommendation for i in session.query(Recommendations).filter(Recommendations.category == id)]
    if not recommendations:
        await callback.message.answer(f'📝 По теме "{category}" пользователи пока ничего не рекомендуют 📝')
        return
    if callback.data:
        await callback.message.answer(f'📝 По теме "{category}" пользователи рекомендуют 📝:')
        for i in recommendations:
            await callback.message.answer(
                text=i,
            )


@dp.callback_query(F.data == 'custom_recommendation')
async def custom_recommendations_handler(callback: types.CallbackQuery, state: FSMContext):
    text = '📝 Выберите тему, по которой вы хотите написать рекомендацию 📝:'
    await state.set_state(RecommendationState.category)
    await callback.message.answer(
        text=text,
        reply_markup=create_recommendations_to_categories_keyboard()
    )


@dp.callback_query(RecommendationState.category, F.data.startswith('add_rec_'))
async def adding_recommendations_handler(callback: types.CallbackQuery, state: FSMContext):
    text = '📝 Введите вашу рекомендацию 📝: '
    await state.set_state(RecommendationState.recommendation)
    await state.update_data(category=int(callback.data.split('_')[-1]))
    await callback.message.answer(
        text=text,
    )

@dp.message(RecommendationState.recommendation)
async def confirm_recommendation_handler(message: types.Message, state: FSMContext):
    session = create_session()
    data = await state.update_data(recommendation=message.text)
    recommendation, category = data['recommendation'], data['category']
    session.add(Recommendations(category=category, recommendation=recommendation))
    await state.clear()
    await message.answer(
        text='Рекомендация успешно добавлена ✅',
    )
    session.commit()