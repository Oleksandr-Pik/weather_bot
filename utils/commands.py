from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Запускає Бота'
        ),
        BotCommand(
            command='help',
            description='Допомога в роботі з Ботом'
        )
    ]
    
    await bot.set_my_commands(commands)