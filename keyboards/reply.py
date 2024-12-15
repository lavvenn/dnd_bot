from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="🔎 Поиск по букве"), KeyboardButton(text="🎲 Броски кубиков")]], resize_keyboard=True)
