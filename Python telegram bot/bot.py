




import asyncpg
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery



TOKEN = "8127358991:AAHbwJ_knmxaaJs7zMfxnXHYKgxW7SZk8Kw"

DB_HOST = "localhost"
DB_NAME = "telegram_bot"
DB_USER = "bot_user"
DB_PASS = "Ben123!!"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def connect_db():
    try:
        conn = await asyncpg.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        print("Database connection successful!")
        await conn.close()

    except Exception as e:
        print(f"Database connection failed: {e}")


async def create_users_table():
    try:
        conn = await asyncpg.connect(
            host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
        )
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                user_id BIGINT UNIQUE,
                username TEXT,
                full_name TEXT,
                created_at TIMESTAMP DEFAULT now()
            )
        """)
        print("✅ Users table created successfully!")
        await conn.close()
    except Exception as e:
        print(f"❌ Failed to create table: {e}")

@dp.message(F.text == '/start')
async def start_command(message: Message):
    conn = await asyncpg.connect(
        host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASS
    )

    await conn.execute("""
    INSERT INTO users (user_id, username, full_name)
    VALUES ($1, $2, $3)
    ON CONFLICT (user_id) DO NOTHING
    """, message.from_user.id, message.from_user.username, message.from_user.full_name)

    await conn.close()

    keyboard = InlineKeyboardMarkup(inline_keyboard=
    [
        [InlineKeyboardButton(text="📖 About", callback_data= "about"),
        InlineKeyboardButton(text="📞 Contact", callback_data="contact")]
    ]
    )
    await message.answer("You have been registered! Choose an option:", reply_markup=keyboard)


@dp.message(F.text == "/help")
async def help_command(message: Message):
    await message.answer("Here are the available commands:\n/start - Start the bot\n/help - Show help menu\n/about - About this bot\n/contact - Contact support")

@dp.callback_query(F.data == "about")
async def about_callback(callback: CallbackQuery):
    await callback.message.answer("This is a test bot created using aiogram v3.")
    await callback.answer()

@dp.callback_query(F.data == "contact")
async def contact_callback(callback: CallbackQuery):
    await callback.message.answer("You can contact support at: @Bahtiyorjon05")
    await callback.answer()


async def main():
    print("🔄 Starting the bot...")
    
    print("🔄 Connecting to the database...")
    await connect_db()

    print("🔄 Creating users table...")
    await create_users_table()

    print("✅ All setup complete. Bot is now running!")
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())  





















# import requests
# import time

# BOT_TOKEN = "8127358991:AAHbwJ_knmxaaJs7zMfxnXHYKgxW7SZk8Kw"
# CHAT_ID = "7050582441"

# URL = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"

# def getUpdates(offset = None):
#     params = {"timeout": 30, "offset": offset}
#     response = requests.get(URL, params)

#     return response.json()

# def process(updates):
#     for update in updates["result"]:
#         chat_id = update["message"]["chat"]["id"]
#         message_text = update["message"]["text"]

#         print(f"New message from {chat_id}: {message_text}")
#         send_message(chat_id, "I received ur message!")

# def send_message(chat_id, message):
#     send_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
#     data = {"chat_id": chat_id, "text": message}
#     requests.post(send_url, json=data)


# offset = None

# while True:
#     updates = getUpdates(offset)

#     if updates["result"]:
#         process(updates)
#         offset = updates["result"][-1]["update_id"] + 1

#     time.sleep(1)













# class Bot:
#     def __init__(self, name, token):
#         self.name = name
#         self.token = token

#     def start(self):
#         print(f"Bot {self.name} is starting with token: {self.token[:5]}****")

#     def send_message(self, chat_id, message):
#         print(f"Sending message to {chat_id}: {message}")

# class PaymeBot(Bot):
#     def __init__(self, name, token, currency):
#         super().__init__(name, token)
#         self.currency = currency

#     def process(self, user_id, amount):
#         print(f"Processing payment of {amount} {self.currency} for user {user_id}")



# bot = PaymeBot("PaymeBot", "123456:gsGdsGSDGSDGSD", "USD")

# bot.start()
# bot.send_message(12341241, "Assalomu alaykum! This is PaymeBot!")
# bot.process(1243513, 100000)