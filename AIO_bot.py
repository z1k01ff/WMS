import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from main import update_time, update_date

TOKEN = "5662776987:AAFNQiftIFBgayordIizZxMeRDcZWCmq7Ao"

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ["Time", "Date", "Поповнення", "Перепаковка"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Дізнайтеся поточний час ", reply_markup=keyboard)


@dp.message_handler(Text(equals="Time"))
async def get_time(message: types.Message):
    update_time()
    with open("time.json") as file:
        current_time = json.load(file)

    await message.answer(current_time)


@dp.message_handler(Text(equals="Date"))
async def get_date(message: types.Message):
    update_date()
    with open("date.json") as file:
        current_date = json.load(file)

    await message.answer(current_date)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)
