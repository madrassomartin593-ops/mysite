import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

TOKEN = "8745560880:AAEbF9JqZ68wCF_UQh82HyBCv9yB6_mJjtM"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer("Привет! Я твой бот 🤖\nНапиши /help чтобы узнать что я умею")

@dp.message(F.text == "/help")
async def help(message: Message):
    await message.answer("Вот что я умею:\n/start — приветствие\n/help — список команд\nпривет — поздороваюсь\nпока — попрощаюсь")

@dp.message(F.text == "привет")
async def hello(message: Message):
    await message.answer("Привет! Как дела? 😊")

@dp.message(F.text == "пока")
async def bye(message: Message):
    await message.answer("Пока! Хорошего дня 👋")
@dp.message(F.text == "как дела")
async def howare(message: Message):
    await message.answer("Отлично,спасибо!") 

@dp.message(F.text == "я учу программирование?")
async def howare(message: Message):
    await message.answer("Да, ты учишь его")


@dp.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())