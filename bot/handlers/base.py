from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from bot.services.api import get_weather_city, get_city_lon_lat
from bot.keyboards.kb import kb

router = Router()


@router.message(CommandStart())
async def command_start(message: Message):
    """обробляємо команду start"""
    await message.answer(f'Привіт {message.from_user.username}')


@router.message(Command('description'))
async def get_description(message: Message):
    await message.answer(text=f'Опис тестового бота', reply_markup=kb)
