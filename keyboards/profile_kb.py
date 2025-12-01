from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text='Профіль'
        )
    ]
],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Для продовження натисніть на кнопку нижче')