import os
import requests
import datetime
from dotenv import load_dotenv
from aiogram import Bot, Router, F
from aiogram.types import Message

load_dotenv()

open_weather_token = os.getenv("WEATHER_API_KEY")

router = Router()


@router.message(F.text == "Погода зараз ⛅")
@router.message()
async def get_weather(message: Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Дощ \U00002614",
        "Thunderstorm": "Гроза \U000026a1",
        "Snow": "Сніг \U0001f328",
        "Mist": "Туман \U0001f32b",
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?"
            f"q={message.text}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Поглянь у вікно, не можу зрозуміти яка там погода!"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(
            data["sys"]["sunset"]
        ) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(
            f"*** {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')} ***\n"
            f"Погода в місті: {city}\n🌡 Температура: {cur_weather}C°\n{wd}\n"
            f"💧 Вологість: {humidity}%\nАтмосферний тиск: {pressure} мм.рт.ст\n🌬 Вітер: {wind} м/с\n"
            f"☀ Схід сонця: {sunrise_timestamp}\n🌜 Захід сонця: {sunset_timestamp}\n⌛ Тривалість дня: {length_of_the_day}\n"
            f"*** Бережіть себе! ***"
        )

    except:
        await message.reply("\U00002620 Перевірте назву міста \U00002620")
