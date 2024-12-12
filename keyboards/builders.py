from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton

from parsing.utils import get_bestiary_by_first_letter


def get_letters_keyboard():
    builder = InlineKeyboardBuilder()

    letters = ["А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]

    for letter in letters:
        builder.add(InlineKeyboardButton(text=letter, callback_data=f"l_{letter}"))
        

    return builder.as_markup()


def get_bestiary_keyboard(first_letter: str, start_from: int = 0, column_height: int = 10) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    bestiary = get_bestiary_by_first_letter(first_letter)

    try:
        for i in range(start_from, column_height + start_from):
            if bestiary[i] == "Астральный эльф почетный караульный": continue
            else:
                print(bestiary[i], i)
                builder.row(InlineKeyboardButton(text=bestiary[i], callback_data=f"b_{bestiary[i]}"))

    except IndexError:
        for i in range(start_from, len(bestiary)):
            builder.row(InlineKeyboardButton(text=bestiary[i], callback_data=f"b_{bestiary[i]}"))

#Астральный эльф почетный караульный
#Арук Громовержец Туунлакалага


    if start_from == 0:
        builder.row(InlineKeyboardButton(text='➡️', callback_data=f'next_{first_letter}_{start_from + column_height}'))

    elif start_from + column_height >= len(bestiary):
        builder.row(InlineKeyboardButton(text='⬅️', callback_data=f'previous_{first_letter}_{start_from - column_height}'))

    else:
        builder.row(InlineKeyboardButton(text='⬅️', callback_data=f'previous_{first_letter}_{start_from - column_height}'),
                    InlineKeyboardButton(text='➡️', callback_data=f'next_{first_letter}_{start_from + column_height}'))
    
    print(start_from, column_height)

    print(f"previous_{first_letter}_{start_from - column_height}")
    print(f"next_{first_letter}_{start_from + column_height}")




    return builder.as_markup()
