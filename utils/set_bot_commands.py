from aiogram import types

async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand('start', 'Запустить бота'),
        types.BotCommand('help', 'Помощь'),
        types.BotCommand('menu', 'Text'),
        types.BotCommand('profilfe', 'Получить данные с БД'),
        types.BotCommand('register', 'Text'),
        types.BotCommand('push_announcement', 'Отправит объявление')

    ])
