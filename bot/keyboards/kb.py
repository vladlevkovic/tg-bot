from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='/description'), KeyboardButton(text='/weather')],
    [KeyboardButton(text='/test'), KeyboardButton(text='/register')]
], resize_keyboard=True)    # клавіатура
