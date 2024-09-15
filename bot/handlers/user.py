from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.services.user_services import user_register

router = Router()


@router.message(Command('register'))
async def register(message: Message):
    user_register(message.from_user.id, message.from_user.username)
    await message.answer('Зареєстровано')
