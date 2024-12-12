from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



back_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️", callback_data="back")
        ]
    ]
)