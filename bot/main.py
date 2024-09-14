from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from weather_data import get_weather_city, get_city_lon_lat
import time
import asyncio


bot = Bot(token='')
dp = Dispatcher()

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/description'), KeyboardButton(text='/weather')],
    [KeyboardButton(text='/test')]
], resize_keyboard=True)    # клавіатура

@dp.message(CommandStart())
async def command_start(message: Message):
    """обробляємо команду start"""
    await message.answer(f'Привіт {message.from_user.username}')


@dp.message(Command('description'))
async def get_description(message: Message):
    await message.answer(text=f'Опис тестового бота', reply_markup=kb)


@dp.message(Command('weather'))
async def get_weather(message: Message):
    lat, lon = get_city_lon_lat()   # отримуємо широту довготу
    weather = get_weather_city(lat, lon)    # словник з погодою у місті
    await message.answer(text=f'Температура - {weather["temp"]}\n'
                              f'Максимальна температура - {weather["temp_max"]}\n'
                              f'Мінімальна температура - {weather["temp_min"]}\n'
                              f'Вологість - {weather["humidity"]}\n'
                              f'Погода - {weather["weather"]}', reply_markup=kb)


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
