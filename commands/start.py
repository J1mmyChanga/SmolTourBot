from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.enums import ParseMode
from create_entities import *
from misc import *


@dp.message(CommandStart())
async def handle_command_start(message: types.Message):
    text = 'Начните работать с нашим ботом'
    kb = [
        [types.KeyboardButton(text='Места для фотосессий')],
        [types.KeyboardButton(text='Советы путешествующим')],
        [types.KeyboardButton(text='Рекомендации от пользователей')],
        [types.KeyboardButton(text='Ответы на частые вопросы')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Выберите кнопку',
    )

    session = create_session()

    if not session.query(Users).filter(Users.user_id==message.from_user.id):
        session.add(Users(user_id=message.from_user.id, first_name=message.from_user.first_name, last_name=message.from_user.last_name))
        text = 'юзер есть'
    await message.answer(
        text=text,
        reply_markup=keyboard,
    )
    session.commit()


@dp.message(Command('help'))
async def handle_command_help(message: types.Message):
    text = markdown.text(
        'Текст который очень помогает',
        sep='\n'
    )
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='Наш сайт',
            url='https://web.telegram.org/k/#-776961079'
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text='Наше мобильное приложение',
            url='https://web.telegram.org/k/#-776961079'
        )
    )
    builder.adjust(1)
    await message.answer(
        text=text,
        parse_mode=None,
        reply_markup=builder.as_markup()
    )