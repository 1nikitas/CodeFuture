import asyncio

from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards import keyboard

bot = Bot(token="5836829227:AAFfBYsJiEZgVhtDhLZuWM4no-Fo4O67e1Q")
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == "/help":
        await message.answer("1 модуль:", reply_markup=keyboard)


# @dp.message_handler(Command('add'))
# async def add(message: types.Message, keyboard=keyboard):
#     info = message.text.split()
#     keyboard = keyboard.add(types.InlineKeyboardButton(
#         text=info[1],
#         url=info[2]))
#     await message.answer("1", reply_markup=keyboard)


async def main1():
    await dp.start_polling()

async def main2():
    while True:
        await asyncio.sleep(1)

async def main_task():
    await asyncio.gather(
        main1(),
        main2()
    )


while True:
    asyncio.get_event_loop().run_until_complete(main_task())