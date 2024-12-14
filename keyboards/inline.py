from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



beast_kb = InlineKeyboardMarkup(
    inline_keyboard=[

            [InlineKeyboardButton(text="📜описание", callback_data="description")],
            [InlineKeyboardButton(text="⬅️назад к выбору", callback_data="back")]
        

    ]
)