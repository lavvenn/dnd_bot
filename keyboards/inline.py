from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



beast_kb = InlineKeyboardMarkup(
    inline_keyboard=[

            [InlineKeyboardButton(text="📜описание", callback_data="description_0")],
            [InlineKeyboardButton(text="⬅️назад к выбору", callback_data="back")]
        

    ]
)

dice_kb = InlineKeyboardMarkup(
    inline_keyboard=[

            [InlineKeyboardButton(text="🟡 D4", callback_data="d4")],
            [InlineKeyboardButton(text="🟠 D6", callback_data="d6")],
            [InlineKeyboardButton(text="🟢 D8", callback_data="d8")],
            [InlineKeyboardButton(text="🔵 D10", callback_data="d10")],
            [InlineKeyboardButton(text="🟣 D12", callback_data="d12")],
            [InlineKeyboardButton(text="🟤 D20", callback_data="d20")],
            [InlineKeyboardButton(text="⬅️назад", callback_data="back")]
        

    ]
)