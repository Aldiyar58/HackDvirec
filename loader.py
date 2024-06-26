from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.db_gino import db

from data import config

# Создоём переменную бота
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

# create Dispatcher
dp = Dispatcher(bot, storage=storage)


_all_ = ['bot', 'storage', 'dp', 'db']
