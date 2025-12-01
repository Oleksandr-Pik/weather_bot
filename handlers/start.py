from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart
from keyboards.start import start_kb
from keyboards.register_kb import register_keyboard
from keyboards.profile_kb import profile_keyboard
from utils.database import Database
import os

router = Router()


@router.message(CommandStart())
async def get_start(message: Message, bot: Bot):
    db = Database(os.getenv("DATABASE_NAME"))
    users = db.select_user_id(message.from_user.id)
    if (users):
        await bot.send_message(
            message.from_user.id,
            f"Привіт, {users[1]}! 🖐\nВкажи назву міста",
            reply_markup=start_kb,
        )
    else:
        await bot.send_message(
            message.from_user.id,
            "Привіт! 🖐\n\n"
            "Цей бот допомагає визначити погоду ⛅ у твоєму місті.\n"
            "Також можна зберегти улюблені міста 🏘\n\n\n"
            "Це та набагато більше буде доступно лише після реєстрації ⬇✅",
            reply_markup=register_keyboard,
        )


# @router.message()
# async def echo(message: Message):
#     await message.answer(f"Ти написав: {message.text}")
