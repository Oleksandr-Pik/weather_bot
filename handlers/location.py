import os
import aiohttp
from aiogram import Router, F
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

router = Router()

OPENWEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@router.message(F.location)
async def get_weather_by_location(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude

    print(lat)
    print(lon)

    async with aiohttp.ClientSession() as session:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric&lang=ua"
        )
        async with session.get(url) as resp:
            data = await resp.json()
            print(data.get("cod"))

    if data.get("cod") != 200:
        await message.answer("Не вдалося отримати погоду 😔")
        return

    city = data["name"]
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]
    wind_speed = data["wind"]["speed"]

    await message.answer(
        f"*** Погода за геолокацією ***\n\n"
        f"📍 Місто: {city}\n"
        f"🌡 Температура: {temp}°C\n"
        f"☁️ Погода: {description.capitalize()}\n"
        f"💧 Вологість: {humidity}%\n"
        f"🔽 Атмосферний тиск: {pressure} hPa\n"
        f"🌬 Швидкість вітру: {wind_speed} м/с"
    )
