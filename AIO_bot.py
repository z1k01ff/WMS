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
    start_buttons = ["Поповнення і Перепаковки", "Відправка"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer("Виберіть бажану функцію", reply_markup=keyboard)


@dp.message_handler(Text(equals="Поповнення і Перепаковки"))
async def popovn_info(message: types.Message):
    # get_popovn()
    with open("test.json") as file:
        popovn = json.load(file)
        result = ""
        for item in popovn.items():
            new_item = str(item)[2:-1].replace("',", " ->")
            result += f"{new_item}\n"

    await message.answer(result)


@dp.message_handler(Text(equals="Відправка"))
async def vidpravka_info(message: types.Message):
    # get_vidpravka()
    with open("vidpravka.json") as file:
        vidpravka = json.load(file)

    await message.answer(vidpravka)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)
