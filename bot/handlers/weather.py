from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from bot.services.api import get_weather_city, get_city_lon_lat
from bot.keyboards.kb import kb
from bot.fsm.city_fsm import CityFSM

router = Router()


# @router.message(Command('weather'))
# async def get_weather(message: Message):
#     lat, lon = get_city_lon_lat()   # отримуємо широту довготу
#     weather = get_weather_city(lat, lon)    # словник з погодою у місті
#     await message.answer(text=f'Температура - {weather["temp"]}\n'
#                               f'Максимальна температура - {weather["temp_max"]}\n'
#                               f'Мінімальна температура - {weather["temp_min"]}\n'
#                               f'Вологість - {weather["humidity"]}\n'
#                               f'Погода - {weather["weather"]}', reply_markup=kb)


@router.message(Command('weather'))
async def request_enter_city(message: Message, state: FSMContext):
    await state.set_state(CityFSM.city)
    await message.answer('Введи назву міста')


@router.message(CityFSM.city)
async def enter_city_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    lat, lon = get_city_lon_lat(message.text)  # отримуємо широту довготу
    weather = get_weather_city(lat, lon)    # словник з погодою у місті
    await state.clear()
    await message.answer(text=f'Температура - {weather["temp"]}\n'
                                  f'Максимальна температура - {weather["temp_max"]}\n'
                                  f'Мінімальна температура - {weather["temp_min"]}\n'
                                  f'Вологість - {weather["humidity"]}\n'
                                  f'Погода - {weather["weather"]}', reply_markup=kb)


