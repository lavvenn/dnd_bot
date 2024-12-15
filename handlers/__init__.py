from aiogram import Router

from handlers.beast_searching import router as beast_searching
from handlers.main import router as main
from handlers.dice import router as dice

router = Router()

router.include_routers(beast_searching,
                       main,
                       dice
                       )