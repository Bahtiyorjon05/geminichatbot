


import os
from transformers import pipeline
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

# Load Hugging Face pipeline
generator = pipeline("text-generation", model="gpt2")

# Function to get response from Hugging Face
def get_huggingface_response(prompt):
    try:
        response = generator(prompt, max_length=50, num_return_sequences=1)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"

# Telegram bot handler functions
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Assalomu alaykum! How can I help you today?")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response = get_huggingface_response(user_message)
    await update.message.reply_text(response)

# Main function
def main():
    TOKEN = "7316067978:AAENPl_zTxjETVdw2QqJTGGN3wlibrMntp8"
    application = Application.builder().token(TOKEN).build()
    
    # Command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
