from aiogram.fsm.state import State, StatesGroup


class CityFSM(StatesGroup):
    city = State()
