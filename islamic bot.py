


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import requests
from apscheduler.schedulers.background import BackgroundScheduler

# Dictionary to store user data (user_id -> city)
user_data = {}

# Function to fetch prayer times using Aladhan API
def get_prayer_times(city: str):
    api_url = f"https://api.aladhan.com/v1/timingsByCity?city={city}&country=Uzbekistan&method=2"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data.get("data") and "timings" in data["data"]:
            return data["data"]["timings"]
        else:
            return None
    else:
        return None

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Set Location", callback_data='set_location'),
            InlineKeyboardButton("Get Prayer Times", callback_data='get_times')
        ],
        [
            InlineKeyboardButton("Subscribe", callback_data='subscribe'),
            InlineKeyboardButton("Unsubscribe", callback_data='unsubscribe')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Assalomu alaykum! 😊 Please choose an option:", reply_markup=reply_markup)

# Button Handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    if query.data == 'set_location':
        await query.message.reply_text("Please type your city name to set your location:")
    elif query.data == 'get_times':
        user_id = query.message.chat_id
        if user_id not in user_data:
            await query.message.reply_text("Please set your location first using the 'Set Location' button.")
        else:
            city = user_data[user_id]
            timings = get_prayer_times(city)
            if timings:
                message = (
                    f"Today's Prayer Times for {city}:\n"
                    f"Fajr: {timings['Fajr']}\n"
                    f"Dhuhr: {timings['Dhuhr']}\n"
                    f"Asr: {timings['Asr']}\n"
                    f"Maghrib: {timings['Maghrib']}\n"
                    f"Isha: {timings['Isha']}"
                )
                await query.message.reply_text(message)
            else:
                await query.message.reply_text(f"Couldn't fetch prayer times for {city}. Please try again.")
    elif query.data == 'subscribe':
        user_id = query.message.chat_id
        if user_id not in user_data:
            await query.message.reply_text("Please set your location first using the 'Set Location' button.")
        else:
            await query.message.reply_text("You are now subscribed to daily prayer time reminders.")
    elif query.data == 'unsubscribe':
        user_id = query.message.chat_id
        if user_id in user_data:
            del user_data[user_id]
            await query.message.reply_text("You are unsubscribed from daily prayer time reminders.")
        else:
            await query.message.reply_text("You are not subscribed to reminders.")

# Command: /setlocation
async def setlocation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat_id
    city = update.message.text.strip()
    if not city:
        await update.message.reply_text("Please provide a valid city name.")
        return

    user_data[user_id] = city

    keyboard = [
        [
            InlineKeyboardButton("Get Prayer Times", callback_data='get_times'),
            InlineKeyboardButton("Main Menu", callback_data='main_menu')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Location set to {city}. What would you like to do next?",
        reply_markup=reply_markup
    )

# Function to send daily reminders
async def send_reminders(context: ContextTypes.DEFAULT_TYPE):
    for user_id, city in user_data.items():
        timings = get_prayer_times(city)
        if timings:
            message = (
                f"Reminder! Today's Prayer Times for {city}:\n"
                f"Fajr: {timings['Fajr']}\n"
                f"Dhuhr: {timings['Dhuhr']}\n"
                f"Asr: {timings['Asr']}\n"
                f"Maghrib: {timings['Maghrib']}\n"
                f"Isha: {timings['Isha']}"
            )
            await context.bot.send_message(chat_id=user_id, text=message)

# Main function
if __name__ == '__main__':
    # Initialize bot
    app = ApplicationBuilder().token('7304838356:AAHsT9zfxeiryB0g-fcbZgQiW264ErAA8oA').build()

    # Add command handlers
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('setlocation', setlocation))
    app.add_handler(CallbackQueryHandler(button_handler))

    # Set up daily reminders
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: app.job_queue.run_once(send_reminders, when=0), 'interval', hours=24)
    scheduler.start()

    # Start bot
    app.run_polling()