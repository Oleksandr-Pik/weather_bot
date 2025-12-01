import os
from aiogram import Bot, Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.register import RegisterState
from utils.database import Database

# router = Router()


async def start_register(message: Message, state: FSMContext, bot: Bot):
    db = Database(os.getenv("DATABASE_NAME"))
    users = db.select_user_id(message.from_user.id)
    if users:
        await bot.send_message(
            message.from_user.id, f"{users[1]} \n Ви вже зареєстровані"
        )
    else:
        await bot.send_message(
            message.from_user.id,
            "🖋 Давайте розпочнемо реєстрацію: \n Для початку напишіть як до вас звертатись?  ⭐",
        )
        await state.set_state(RegisterState.regName)


async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"🙂 Приємно, познайомитись, {message.text} \n"
        "А тепер вкажи з якого ти міста? 🏘",
    )
    await state.update_data(regname=message.text)
    await state.set_state(RegisterState.regCity)


async def register_city(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        f"🙂 Ти вказав, що твоє місто 🏘 {message.text} \n\n"
        "Чудово тепер можна буде дізнаватись погоду ⛅ у твоєму місті.",
    )
    await state.update_data(regcity=message.text)
    reg_data = await state.get_data()
    reg_name = reg_data.get("regname")
    reg_city = reg_data.get("regcity")
    msg = f"Реєстрацію завершено! ✅\n\n Ім'я - {reg_name}\n місто - {reg_city}"
    await bot.send_message(message.from_user.id, msg)
    db = Database(os.getenv("DATABASE_NAME"))
    db.add_user(reg_name, reg_city, message.from_user.id)
    await state.clear()
