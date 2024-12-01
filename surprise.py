


import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Send a countdown to build suspense
    await update.message.reply_text("1...")
    await asyncio.sleep(1)  # Wait for 1 second
    await update.message.reply_text("2...")
    await asyncio.sleep(1)  # Wait for 1 second
    
    # After countdown, send the final message with heart
    heart = "❤️"
    response = f"I missed you! {heart}"
    await update.message.reply_text(response)

# Main function to start the bot
def main():
    # Replace 'YOUR_API_TOKEN' with the token you got from BotFather
    application = ApplicationBuilder().token("8053467913:AAEofpg73vbgl4RFK_dnngv-1bHbAjso17A").build()

    # Add the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot
    print("I Missed You Surprise Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
