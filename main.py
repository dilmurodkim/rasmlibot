from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, FSInputFile
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
import asyncio

TOKEN = '7608303461:AAEAD7P2vnZ6rvWb_kXGj-gaQHyic9alYFs'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📷 Rasmni ko'rish", callback_data="show_image")
    await message.answer("Quyidagi tugmani bosing rasmni ko‘rish uchun:", reply_markup=builder.as_markup())


@dp.callback_query(F.data == "show_image")
async def show_image_handler(callback: types.CallbackQuery):
    image = FSInputFile("media/image1.jpg")
    await callback.message.answer_photo(photo=image, caption="Mana rasm!")
    await callback.answer()  # callback tugmasi bosilgani haqida javob


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
