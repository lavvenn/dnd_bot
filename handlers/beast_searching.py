from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from states import Search_beast

from keyboards.builders import get_bestiary_keyboard, get_letters_keyboard, get_beast_description_keyboard
from keyboards.inline import beast_kb

from parsing.utils import get_beast_description, get_beast_abilities, get_beast_small_description


router = Router()


LETTER_CHOICE_MESSAGE = """
🔍 Время искать! 🔍
Похоже, вы хотите узнать о каком-то существе из нашего бестиария. Чтобы помочь вам быстрее, пожалуйста, выберите первую букву названия существа, которое вы ищете. Просто напишите букву, и я открою перед вами двери в мир удивительных созданий! 🦄🐉
💡 Например: Если вы ищете "Дракона", просто нажмите "Д"!
Жду вашего выбора! ✨
"""

BEAST_CHOICE_MESSAGE = """
🌟 Отлично! 🌟
Теперь, когда вы выбрали первую букву, давайте продолжим! Ниже представлены существа, начинающиеся на эту букву. Выберите одно из них, чтобы узнать больше о его характеристиках и способностях! 🦄🐉
"""


@router.message(F.text == "🔎 Поиск по букве")
async def search_by_letter(message: Message, state: FSMContext):
    await message.answer(LETTER_CHOICE_MESSAGE, reply_markup=get_letters_keyboard())
    await state.set_state(Search_beast.choise_letter)


@router.callback_query(Search_beast.choise_letter)
async def choice_letter(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(BEAST_CHOICE_MESSAGE, reply_markup=get_bestiary_keyboard(callback.data))
    await state.update_data(letter=callback.data)
    await state.set_state(Search_beast.choise_beast)


@router.callback_query(F.data.startswith("next"), Search_beast.choise_beast)
async def next_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.edit_text(BEAST_CHOICE_MESSAGE, reply_markup=get_bestiary_keyboard(first_letter=data["letter"],start_from=int(callback.data[5:])))


@router.callback_query(F.data.startswith("previous"), Search_beast.choise_beast)
async def previous_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await callback.message.edit_text(BEAST_CHOICE_MESSAGE, reply_markup=get_bestiary_keyboard(first_letter=data["letter"],start_from=int(callback.data[9:])))


@router.callback_query(Search_beast.choise_beast)
async def choice_beast(callback: CallbackQuery, state: FSMContext):

    await state.set_state(Search_beast.beast_description)

    beast_name = callback.data

    await state.update_data(beast_name=beast_name)

    beast_abilities = get_beast_abilities(beast_name)

    beast_description = get_beast_small_description(beast_name)


    beast_description = f"""
👤{beast_name}

📜{beast_description[0]}
🛡️{beast_description[1]}
⚔️{beast_description[2]}
🏃{beast_description[3]}

💪сила -> {beast_abilities[0]}
🏃‍♂️ловкость -> {beast_abilities[1]}
🏋️‍♂️Телосложение -> {beast_abilities[2]}
🧠Интеллект -> {beast_abilities[3]}
👁️‍🗨️Мудрость -> {beast_abilities[4]}
✨Харизма -> {beast_abilities[5]}
"""
    
    await callback.message.edit_text(beast_description, reply_markup=beast_kb)


@router.callback_query(F.data.startswith("description_"), Search_beast.beast_description)
async def beast_description(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    beast_name = data["beast_name"]
    beast_description_list = get_beast_description(beast_name)

    await callback.message.edit_text(f"""
👤{beast_name}

📜{int(callback.data[12:]) + 1}
{beast_description_list[int(callback.data[12:])]}""", reply_markup=get_beast_description_keyboard(beast_description_list))
    

@router.callback_query(F.data == "back_to_abilities", Search_beast.beast_description)
async def back_to_abilities(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    beast_name = data["beast_name"]

    beast_abilities = get_beast_abilities(beast_name)

    beast_description = get_beast_small_description(beast_name)

    beast_description = f"""
👤{beast_name}

📜{beast_description[0]}
🛡️{beast_description[1]}
⚔️{beast_description[2]}
🏃{beast_description[3]}

💪сила -> {beast_abilities[0]}
🏃‍♂️ловкость -> {beast_abilities[1]}
🏋️‍♂️Телосложение -> {beast_abilities[2]}
🧠Интеллект -> {beast_abilities[3]}
👁️‍🗨️Мудрость -> {beast_abilities[4]}
✨Харизма -> {beast_abilities[5]}
"""
    
    await callback.message.edit_text(beast_description, reply_markup=beast_kb)
    


@router.callback_query(F.data == "back")
async def back_to_menu(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Search_beast.choise_letter)
    await callback.message.edit_text(LETTER_CHOICE_MESSAGE, reply_markup=get_letters_keyboard())