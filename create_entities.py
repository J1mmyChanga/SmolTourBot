from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from config import settings
from data import *


dp = Dispatcher()
bot = Bot(
    token=settings.bot_token,
    parse_mode=ParseMode.MARKDOWN_V2
)

global_init('db/bot.db')