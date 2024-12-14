from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Search_beast(StatesGroup):
    choise_letter = State()
    choise_beast = State()
    beast_description = State()