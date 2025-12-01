import os
import asyncio

from dotenv import load_dotenv
from aiogram.filters import Command
from aiogram import Bot, Dispatcher, F
from utils.commands import set_commands
from state.register import RegisterState
from handlers import location, get_weather
from handlers.start import router as start_router
from handlers.register import start_register, register_name, register_city
from filters.CheckAdmin import CheckAdmin


load_dotenv()

token = os.getenv("TG_TOKEN")
admin_id = os.getenv("ADMIN_ID")
super_admin_id = 731044153

bot = Bot(token=token)
dp = Dispatcher()

dp.include_router(start_router)

dp.message.register(start_register, F.text == "Зареєструватись")
dp.message.register(register_name, RegisterState.regName)
dp.message.register(register_city, RegisterState.regCity)

dp.include_routers(
    location.router, 
    get_weather.router
)


async def start_bot(*_):
    print("Бот стартує...")
    await bot.send_message(super_admin_id, text="Бот запущено")


dp.startup.register(start_bot)


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
