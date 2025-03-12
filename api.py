





# import os
# from telegram import Update
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
# import google.generativeai as genai

# # Configure the Gemini API
# GEMINI_API_KEY = "AIzaSyBWKnFL4v8azBIzxjlRIT-3gZd89w1WRVU"
# genai.configure(api_key=GEMINI_API_KEY)

# # Telegram bot token from BotFather
# TELEGRAM_BOT_TOKEN = "7316067978:AAENPl_zTxjETVdw2QqJTGGN3wlibrMntp8"

# # Function to query Gemini API with chat history
# def ask_gemini(history: list) -> str:
#     try:
#         # Convert our history format to Gemini's expected format
#         gemini_history = [{"parts": [{"text": item["content"]}], "role": item["role"]} for item in history]
#         response = genai.GenerativeModel('gemini-2.0-flash').generate_content(gemini_history)
#         return response.text
#     except Exception as e:
#         return f"Oops, something went wrong: {str(e)}"

# # Command handler for /start
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     context.user_data["history"] = []  # Initialize chat history
#     welcome_message = "I’m your Gemini-powered bot. I’ll remember our chat. What’s your name or question?"
#     context.user_data["history"].append({"role": "assistant", "content": welcome_message})
#     await update.message.reply_text(welcome_message)

# # Message handler for user questions
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     user_message = update.message.text
#     user_data = context.user_data

#     # Initialize history if not present
#     if "history" not in user_data:
#         user_data["history"] = []

#     # Check if user is introducing their name
#     if "my name is" in user_message.lower():
#         name = user_message.lower().split("my name is")[-1].strip()
#         user_data["name"] = name.capitalize()
#         response = f"Got it, {user_data['name']}. What’s your question?"
#         user_data["history"].append({"role": "user", "content": user_message})
#         user_data["history"].append({"role": "assistant", "content": response})
#     else:
#         # Add user message to history
#         user_data["history"].append({"role": "user", "content": user_message})
#         # Query Gemini with full history
#         gemini_response = ask_gemini(user_data["history"])
#         # Add Gemini's response to history
#         user_data["history"].append({"role": "assistant", "content": gemini_response})
#         response = gemini_response

#     await update.message.reply_text(response)

# # Command handler for /forget
# async def forget(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     context.user_data.clear()
#     await update.message.reply_text("Memory wiped. Fresh start.")

# # Error handler
# async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     print(f"Update {update} caused error {context.error}")
#     await update.message.reply_text("Something broke. I’ll recover soon.")

# # Main function to run the bot
# def main():
#     print("Starting Telegram bot...")
    
#     # Create the Application and pass the bot token
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

#     # Add handlers
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(CommandHandler("forget", forget))
#     application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
#     application.add_error_handler(error)

#     # Start the bot
#     application.run_polling(allowed_updates=Update.ALL_TYPES)

# if __name__ == "__main__":
#     main()




from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Configure the Gemini API
GEMINI_API_KEY = "AIzaSyBWKnFL4v8azBIzxjlRIT-3gZd89w1WRVU"
genai.configure(api_key=GEMINI_API_KEY)

# Telegram bot token from BotFather
TELEGRAM_BOT_TOKEN = "7316067978:AAENPl_zTxjETVdw2QqJTGGN3wlibrMntp8"

# Function to query Gemini API with chat history
def ask_gemini(history: list) -> str:
    try:
        # Convert our history format to Gemini's expected format
        gemini_history = [{"parts": [{"text": item["content"]}], "role": item["role"]} for item in history]
        response = genai.GenerativeModel('gemini-1.5-flash').generate_content(gemini_history)  # Using 1.5-flash
        return response.text
    except Exception as e:
        return f"Oops, something went wrong: {str(e)}"

# Function to send long messages in parts
async def send_long_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    MAX_LENGTH = 4000  # Telegram limit is 4096, leave buffer
    for i in range(0, len(text), MAX_LENGTH):
        chunk = text[i:i + MAX_LENGTH]
        await update.message.reply_text(chunk)

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["history"] = []  # Initialize chat history
    welcome_message = "I’m your Gemini-powered bot. I’ll remember our chat. What’s your name or question?"
    context.user_data["history"].append({"role": "assistant", "content": welcome_message})
    await update.message.reply_text(welcome_message)

# Message handler for user questions
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_data = context.user_data

    # Initialize history if not present
    if "history" not in user_data:
        user_data["history"] = []

    # Check if user is introducing their name
    if "my name is" in user_message.lower():
        name = user_message.lower().split("my name is")[-1].strip()
        user_data["name"] = name.capitalize()
        response = f"Got it, {user_data['name']}. What’s your question?"
        user_data["history"].append({"role": "user", "content": user_message})
        user_data["history"].append({"role": "assistant", "content": response})
        await update.message.reply_text(response)
    else:
        # Add user message to history
        user_data["history"].append({"role": "user", "content": user_message})
        # Query Gemini with full history
        gemini_response = ask_gemini(user_data["history"])
        # Add Gemini's response to history
        user_data["history"].append({"role": "assistant", "content": gemini_response})
        # Send long response in parts
        await send_long_message(update, context, gemini_response)

# Command handler for /forget
async def forget(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text("Memory wiped. Fresh start.")

# Error handler
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    if "Message is too long" in str(context.error):
        await update.message.reply_text("Oops, response was too long! Trying to send in parts...")
    else:
        await update.message.reply_text("Something broke. I’ll recover soon.")

# Main function to run the bot
def main():
    print("Starting Telegram bot...")
    
    # Create the Application and pass the bot token
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("forget", forget))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error)

    # Start the bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()