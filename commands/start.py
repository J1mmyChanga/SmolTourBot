from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.utils import markdown
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.enums import ParseMode
from create_entities import *
from misc import *


@dp.message(CommandStart())
async def handle_command_start(message: types.Message):
    text = '🔎 Начните пользоваться нашим ботом 🔎'
    kb = [
        [types.KeyboardButton(text='📸 Места для фотосессий 📸')],
        [types.KeyboardButton(text='📒 Советы путешественникам 📒')],
        [types.KeyboardButton(text='✉ Рекомендации от пользователей ✉')],
        [types.KeyboardButton(text='❓ Ответы на частые вопросы ❓')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Выберите кнопку',
    )
    await message.answer(
        text=text,
        reply_markup=keyboard,
    )
    session.commit()


@dp.message(Command('help'))
async def handle_command_help(message: types.Message):
    text = markdown.text(
        '📸 Привет, SmolTour - твой виртуальный проводник в удивительный мир путешествий в Смоленске! 🌍✨\n',
        '🏞️ Исследуй город с лучшими видами! Отправляйся в раздел "📸 Места для фотосессий 📸" и открывай перед собой картину красивейших мест для фотосессий. 📷🏰\n',
        '🌟 В разделе "📋 Советы путешественникам 📋" я подскажу тебе, как сделать свое путешествие незабвенным! Не забудь заглянуть, чтобы узнать лайфхаки от настоящих путешественников. 🧳🗝️\n',
        '🤝 Обменяйся опытом с другими участниками SmolTour! В "✉ Рекомендации от пользователей ✉" ты найдешь рекомендации, которые станут невероятным дополнением к твоему путеводителю. 👥🗨️\n',
        '❓ Вопросы? Нет проблем! В разделе "❓ Ответы на частые вопросы ❓" я подготовил ответы на самые часто задаваемые вопросы, чтобы твое путешествие было максимально комфортным.⁉️💼\n',
        'Открой для себя Смоленск в новом свете с SmolTour - твоим верным спутником в мире туризма и культуры! 🌆🗺️\n',
        sep=' \n '
    )
    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text='🖥 Наш сайт 🖥',
            url='https://umom.pro/'
        )
    )
    builder.add(
        types.InlineKeyboardButton(
            text='📱 Наше мобильное приложение 📱',
            url='https://web.telegram.org/k/#-776961079'
        )
    )
    builder.adjust(1)
    await message.answer(
        text=text,
        parse_mode=None,
        reply_markup=builder.as_markup()
    )