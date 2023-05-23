from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # pip install aiogram
from aiogram import Dispatcher, Bot, executor, types
import json

API_TOKEN = "5662776987:AAFNQiftIFBgayordIizZxMeRDcZWCmq7Ao"

# инициализация ботика...
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot)

# Создание клавиатуры
btn_berta = KeyboardButton("🎲 Берта")
btn_blyzenko = KeyboardButton('🔐 Близенько')
btn_other = KeyboardButton("🔷 Другое")



btn_info = KeyboardButton('ℹ️ Информация')
btn_main = KeyboardButton('🟡 Главное меню')
btn_back = KeyboardButton('🟡 Назад')

btn_berta_popovn = KeyboardButton('☮ Поповнення')
btn_berta_vidpravka = KeyboardButton('☯ Відправка')
btn_berta_postavka = KeyboardButton('✡ Транспорт поставка')

btn_blyzenko_peremisch = KeyboardButton('ℹ️ Б Переміщення')
btn_blyzenko_popovn = KeyboardButton('ℹ️ Б Поповнення')


main_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_berta, btn_blyzenko, btn_other)
other_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_info, btn_main)
berta_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_berta_postavka, btn_berta_popovn, btn_berta_vidpravka, btn_back)
blyzenko_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_blyzenko_popovn, btn_blyzenko_peremisch, btn_back)



@dispatcher.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f"👋 Привет, {message.from_user.first_name}!", reply_markup=main_menu)


@dispatcher.message_handler()
async def messages(message: types.Message):
    if message.text == "🎲 Берта":
        await bot.send_message(message.from_user.id, '🟡 Открываю меню Берта...', reply_markup=berta_menu)
    elif message.text == '🔐 Близенько':
        await bot.send_message(message.from_user.id, '🟡 Открываю меню Близенько...', reply_markup=blyzenko_menu)
    elif message.text == '🔷 Другое':
        await bot.send_message(message.from_user.id, '🔷 Открываю...', reply_markup=berta_menu)
    elif message.text == 'ℹ️ Відправка':
        with open("../app/json data/kilkist_vidpravok.json") as file:
            json_file = json.load(file)
        await message.answer(json_file)
    elif message.text == '🟡 Назад':
        await bot.send_message(message.from_user.id, '🟡 Открываю меню...', reply_markup=main_menu)
    else:
        await bot.send_message(message.from_user.id, f'😐 Ботик вас не понял... :(')


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)