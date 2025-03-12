import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BOT_TOKEN

# Enable logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Main menu inline keyboard
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📝 Sign Up", callback_data="signup"),
        InlineKeyboardButton(text="🔑 Login", callback_data="login"),
    ],
    [
        InlineKeyboardButton(text="🔒 Forgot Password", callback_data="forgot_password"),
        InlineKeyboardButton(text="👨‍💼 Admin Login", callback_data="admin_login"),
    ],
    [
        InlineKeyboardButton(text="❓ Help & FAQ", callback_data="help_faq"),
        InlineKeyboardButton(text="🌍 Select Language", callback_data="select_language"),
    ],
    [
        InlineKeyboardButton(text="📞 Contact Support", callback_data="contact_support"),
        InlineKeyboardButton(text="⚠️ Report Issue", callback_data="report_issue"),
    ]
])

# Start Command Handler
@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    await message.answer(
        "👋 *Welcome to PaymeBot!*\n\nSelect an option from the Main Menu:", 
        reply_markup=main_menu,
        parse_mode="Markdown"
    )

# Main function to run the bot
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
