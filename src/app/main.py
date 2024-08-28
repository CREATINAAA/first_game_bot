import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import BotCommand

from ..service.user_private import user_private_router
from . import settings

ALLOWED_UPDATES = ["message, edited_message"]
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(user_private_router)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/menu", description="Показать меню"),
        BotCommand(command="/help", description="Помощь и доступные команды"),
    ]
    await bot.set_my_commands(commands)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #         ^^^^ скипаем все обновления, которые прилетели во время того, как бот лежал
    await dp.start_polling(bot, on_startup=set_commands)


asyncio.run(main())
