import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from selenium_to_txt import json_open

TOKEN = "5662776987:AAFNQiftIFBgayordIizZxMeRDcZWCmq7Ao"

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Поповнення", "Відправка"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Виберіть бажану функцію", reply_markup=keyboard)


@dp.message_handler(Text(equals="Поповнення"))
async def popovn_info(message: types.Message):
    await message.answer(json_open("kilkist_popovnen"))


@dp.message_handler(Text(equals="Відправка"))
async def vidpravka_info(message: types.Message):
    await message.answer(json_open("kilkist_vidpravok"))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)

