import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
import os

# Aapka Token yahan hai
BOT_TOKEN = "9184649691:AAGLQpVMDIsN8Zjn0WlR9A3yQaVusLf73r8"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: Message):
    user_name = message.from_user.first_name
    
    welcome_text = (
        f"🛒 ─────── **TUN TUN 2** ─────── 🛒\n\n"
        f"👑 <i>Welcome, {user_name}</i>\n\n"
        f"🔥 ── **STORE HIGHLIGHTS** ── 🔥\n\n"
        f"🎰 **Premium Game Keys**\n"
        f"🟢 Instant Delivery 24/7\n"
        f"💯 100% Secure Payment\n"
        f"🏷️ Best Prices Guaranteed\n"
        f"🇮🇳 Safe And Trusted\n"
        f"✅ Professional Support\n\n"
        f"────────────────────\n"
        f"💰 **Wallet Balance:** ₹0.00\n"
        f"────────────────────\n\n"
        f"🔥 <i>Tap Shop Now to Start!</i>"
    )

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🛒 Shop / Store Product", callback_data="shop")],
        [
            InlineKeyboardButton(text="🪙 Add Balance", callback_data="add_balance"),
            InlineKeyboardButton(text="👑 My Profile", callback_data="profile")
        ],
        [
            InlineKeyboardButton(text="🥇 How To Use", callback_data="how_to"),
            InlineKeyboardButton(text="🎁 Lucky", callback_data="lucky")
        ],
        [
            InlineKeyboardButton(text="➡️ Share", callback_data="share"),
            InlineKeyboardButton(text="🔔 Support", callback_data="support")
        ]
    ])

    await message.answer(welcome_text, reply_markup=keyboard, parse_mode=ParseMode.MARKDOWN)

@dp.callback_query(F.data == "shop")
async def shop_handler(callback: CallbackQuery):
    await callback.answer("Shop khul raha hai...", show_alert=False)
    await callback.message.answer("🛒 Yahan aapke saare products aayenge.")

@dp.callback_query(F.data == "add_balance")
async def balance_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("💰 Balance add karne ke liye UPI par pay karein.")

@dp.callback_query(F.data == "profile")
async def profile_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("👑 Aapki Profile:\nName: User\nBalance: ₹0.00")

async def main():
    print("Bot Start Ho Gaya Hai...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
