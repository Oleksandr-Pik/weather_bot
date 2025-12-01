from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        # [KeyboardButton(text="Погода зараз ⛅")],
        [KeyboardButton(text="Погода за геолокацією 📍", request_location=True)],
        # [KeyboardButton(text="Мої міста 🏘")],
        [KeyboardButton(text="Київ")],
        [KeyboardButton(text="Львів")],
        [KeyboardButton(text="Одеса")],
        [KeyboardButton(text="Херсон")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
