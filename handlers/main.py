from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

from keyboards.builders import get_bestiary_keyboard, get_letters_keyboard
from keyboards.reply import main_kb
from keyboards.inline import back_button
from parsing.utils import get_beast_description

router = Router()

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer("Welcome!", reply_markup=main_kb)


@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("help maessage")


@router.message(F.text == "🔎 Поиск по букве")
async def search_by_letter(message: Message):
    await message.answer("Выберите букву", reply_markup=get_letters_keyboard())


@router.callback_query(F.data.startswith("next"))
async def callback_query_handler(callback: CallbackQuery):
    print(callback.data[5:], " ", callback.data[7:])
    await callback.message.edit_text("Welcome!", reply_markup=get_bestiary_keyboard(first_letter=str(callback.data[5]),start_from=int(callback.data[7:])))


@router.callback_query(F.data.startswith("previous"))
async def callback_query_handler(callback: CallbackQuery):
    await callback.message.edit_text("Welcome!", reply_markup=get_bestiary_keyboard(first_letter=str(callback.data[9]),start_from=int(callback.data[11:])))


@router.callback_query(F.data.startswith("b_"))
async def callback_query_handler(callback: CallbackQuery):
    beast_name = callback.data[2:]
    beast_description = get_beast_description(beast_name)
    await callback.message.edit_text(beast_description, reply_markup=back_button)


@router.callback_query(F.data.startswith("l_"))
async def callback_query_handler(callback: CallbackQuery):
    await callback.message.edit_text("выберите челика", reply_markup=get_bestiary_keyboard(callback.data[2:]))


@router.callback_query(F.data == "back")
async def callback_query_handler(callback: CallbackQuery):
    await callback.message.edit_text("выберите букву", reply_markup=get_letters_keyboard())