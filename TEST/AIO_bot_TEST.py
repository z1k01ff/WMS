import asyncio
import json

from aiogram import Bot, Dispatcher, executor, types
# from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from WMS_main_TEST import wms_vidpravka, wms_login, wms_popovn, wms_tp_fast, wms_exit
from selenium_to_text import json_to_text

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
    # kilkist_popovn = "Дата оновлення\n" + json_to_text("kilkist_popovnen")
    # await message.answer(kilkist_popovn)
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
    # wms_tp_fast(wms_login())
    # wms_popovn(wms_login())
    # wms_vidpravka(wms_login())
    # wms_exit(wms_login())

