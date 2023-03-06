import haders_a

from aiogram import Bot, Dispatcher
from config_a import load_config

API_TOKEN: str = load_config().tg_bot.token

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


dp.include_router(haders_a.router)


if __name__ == '__main__':
    dp.run_polling(bot)
