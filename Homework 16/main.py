import asyncio
import time

from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
import os

from aiogram.filters import Command

from configs import get_values
from kuyboards import button_category
from parsed_data import parser_travel

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = Bot(
    TOKEN,
    default=DefaultBotProperties(parse_mode='HTML')
)

dp = Dispatcher()

@dp.message(Command("start"))
async def command_start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Hello, <b>{full_name}</b>\n"
                         f"Wellcome our bot🤩")
    await show_category_button(message)

async def show_category_button(message: Message):
    await message.answer("Choose one category below 👇", reply_markup=button_category())

@dp.message()
async def get_product_by_techno_shop(message: Message):
    category_text = message.text

    category_key = get_values(category_text)
    if category_key is None:
        return await message.answer(
            "Sorry this kind of category is not available🥺!"
            "Please choose another category🥹"
        )

    get_product = parser_travel(category_key)
    if not get_product:
        return await message.answer(
            "Sorry nothing found in this category🥶"
        )

    for product in get_product:
        images = product.get('image')
        title = product.get('title')
        price = product.get('price')
        availability = product.get('availability')

        time.sleep(0.5)

        await message.answer_photo(
            photo=images,
            caption=f"{title}\n\n{price}\n\n{availability}"
        )


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())