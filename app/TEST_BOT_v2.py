from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from DB import privyazka


bot = Bot(token="5662776987:AAFNQiftIFBgayordIizZxMeRDcZWCmq7Ao")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text="Прив'язка"))
    keyboard.add(types.KeyboardButton(text="Відправка"))
    await message.reply("Привіт! Я Telegram бот.", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == "Прив'язка")
async def handle_topup(message: types.Message):
    await message.reply("Введіть артикул:")

    # Зберігаємо ID користувача та текст повідомлення в контексті
    await bot.get_chat_member(message.chat.id, message.from_user.id)
    context = dp.current_state(user=message.from_user.id)
    await context.set_state('waiting_for_text')


@dp.message_handler(state='waiting_for_text')
async def process_topup_text(message: types.Message, state: State):
    # Отримуємо текст з повідомлення
    text = message.text


    # Викликаємо функцію для обробки поповнення з текстом
    test = privyazka(text)

    # Скидаємо стан
    await state.finish()

    with open("../app/privyazka.png", 'rb') as photo:
        await bot.send_photo(message.chat.id, photo)

    # Відправляємо відповідь користувачу
    # await message.reply("Поповнення оброблено.")
    # await message.reply(test)


# async def handle_topup_text(topup_text: str):
#     # Ваша логіка обробки поповнення з використанням тексту `topup_text`
#     print(f"Поповнення з текстом: {topup_text}")


if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
