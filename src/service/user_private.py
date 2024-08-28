from aiogram import types, Router
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart

from .keyboards import get_start_keyboard


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start(message: types.Message):
    image_path = 'first_game_bot/static/141042.webp'
    await message.answer_photo(photo=FSInputFile(image_path), caption="Сыграем в игру?", reply_markup=get_start_keyboard())
