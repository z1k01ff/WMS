import asyncio
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

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
    with open("../TEST/kilkist_popovnen.json") as file:
        json_file = json.load(file)

    await message.answer(json_file)


@dp.message_handler(Text(equals="Відправка"))
async def vidpravka_info(message: types.Message):
    with open("../TEST/kilkist_vidpravok.json") as file:
        json_file = json.load(file)

    await message.answer(json_file)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)

