from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from keyboards.reply import main_kb


router = Router()



WELLCOME_MESSAGE = """
🌟 Добро пожаловать, отважные искатели приключений! 🌟
Я ваш верный помощник в мире ДНД, готовый помочь вам на каждом шагу! 🎲✨
Вот что я могу предложить:
📚 Справочник (бестиарий): Узнайте о самых удивительных существах!
🔮 Список заклинаний: Откройте для себя магию и её эффекты.
🎲 Броски кубиков: Я совершу броски, чтобы вы могли сосредоточиться на стратегии!
🛡️ Создание персонажа: Давайте вместе разработаем вашего уникального героя!
Что бы вы хотели сделать в первую очередь? 🤔💭 Пусть ваше приключение начнется! 🏰🌌
"""



@router.message(CommandStart())
async def start_cmd(message: Message,state: FSMContext):
    state.clear()
    await message.answer(WELLCOME_MESSAGE, reply_markup=main_kb)


@router.message(Command("help"))
async def help_cmd(message: Message):
    await message.answer("help maessage")