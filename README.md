# Weather Bot

A simple and user-friendly Telegram bot that provides real-time weather information for any city.  
Built with **Python** and **Aiogram**.

## Features

- Get current weather by sending a city name  
- Weather retrieval via external API (e.g., OpenWeatherMap)  
- Support for location-based weather requests  
- User registration flow (name + city)  
- Custom keyboards for improved interaction  
- Admin check filter  
- Structured and scalable project architecture

## Project Structure

weather_bot/
│
├── filters/ # Custom filters (e.g., admin checking)
├── handlers/ # Message & command handlers
│ ├── start.py
│ ├── location.py
│ ├── get_weather.py
│ └── register.py
│
├── keyboards/ # Reply keyboards (start, register, profile)
│
├── state/ # FSM states for registration
│
├── utils/ # Helper utilities (commands, database)
│ ├── commands.py
│ └── database.py
│
├── main.py # Main bot entry point
├── .env.example # Example environment configuration
├── requirements.txt # Project dependencies
└── README.md

## Requirements

- Python 3.10+
- Telegram Bot Token (from BotFather)
- Weather API key (e.g., from OpenWeatherMap)
- All libraries listed in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Oleksandr-Pik/weather_bot.git
   cd weather_bot

2. Create and activate a virtual environment:

```bash

python -m venv venv
source venv/bin/activate       # Linux / macOS
venv\Scripts\activate          # Windows
```

3. Install dependencies:

```bash

pip install -r requirements.txt

```

4. Create the .env file:

```env

TELEGRAM_TOKEN=your_telegram_token_here
WEATHER_API_KEY=your_weather_api_key_here
ADMIN_ID=your_telegram_id
```

5. Run the bot:

```bash
python main.py
```

## Usage

- Send /start to begin
- Follow the prompts to register your name and city (optional)
- Type any city name to get the current weather
- Share your location to get weather for your exact coordinates

## Technologies Used

- Aiogram — Telegram Bot API framework
- Aiohttp — async HTTP requests
- Requests — sync HTTP requests
- SQLite — local data storage
- python-dotenv — environment variable management

## Future Improvements

- Multi-language support

- 3-day or 7-day forecast

- Inline buttons with quick city selection

- Improved error handling

- Weather icons & formatted messages

## License

This project is open-source. You may use and modify it as you wish.