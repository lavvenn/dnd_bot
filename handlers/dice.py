from random import randint
from time import sleep

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


from keyboards.inline import dice_kb


from states import Dice


router = Router()


@router.message(F.text == "🎲 Броски кубиков")
async def dice(message: Message, state: FSMContext):
    await state.set_state(Dice.selest_dice)
    await message.delete()
    await message.answer("🎲 Выберите кубик для броска", reply_markup=dice_kb)

@router.callback_query(F.data.startswith("d"), Dice.selest_dice)
async def dice(callback: CallbackQuery, state: FSMContext):
    for i in range(3):
        await callback.message.edit_text(f"{3-i}...")
        sleep(1)

    dice = int(callback.data[1:])
    result = randint(1, dice)
    await callback.message.edit_text(f"Вы бросили кубик D{dice}\nполучили {result}🎲")

