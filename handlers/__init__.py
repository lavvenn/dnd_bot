from aiogram import Router

from handlers.main import router as main

router = Router()

router.include_routers(main
                       )