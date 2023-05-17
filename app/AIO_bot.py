import asyncio
import json

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from WMS_main import wms_tp, wms_login, wms_popovn

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
    # get_popovn()
    with open("kilkist_popovn.json") as file:
        popovn = json.load(file)
        result2 = ""
        for item in popovn.items():
            new_item = str(item)[2:-1].replace("',", " ->")
            result2 += f"{new_item}\n"

    await message.answer(result2)


@dp.message_handler(Text(equals="Відправка"))
async def vidpravka_info(message: types.Message):
    # get_vidpravka()
    with open("kilkist_tp.json") as file:
        vidpravka = json.load(file)
        result = ""
        for item in vidpravka.items():
            new_item = str(item)[2:-1].replace("',", " ->")
            result += f"{new_item}\n"

    await message.answer(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp)
    wms_tp(wms_login())
    wms_popovn(wms_login())
