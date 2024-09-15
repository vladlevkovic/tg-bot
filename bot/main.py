from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from bot.handlers import base, weather, user
import asyncio
import os

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

async def main():
    dp.include_router(base.router)
    dp.include_router(weather.router)
    dp.include_router(user.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
