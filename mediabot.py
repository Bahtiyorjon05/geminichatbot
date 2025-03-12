

#    Instagram, YouTube, LinkedIn video download bot

import telebot
import yt_dlp
import os
import time
import logging
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Bot token from BotFather
BOT_TOKEN = '7665537600:AAHggN60xuyzXP2gO_Us1Yg18IoDOLHa-6s'
bot = telebot.TeleBot(BOT_TOKEN)

# Bot Handlers
@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "unknown"
    first_name = message.from_user.first_name or "Unknown"
    last_name = message.from_user.last_name or "Unknown"
    
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    phone_button = KeyboardButton("📱 Share Contact", request_contact=True)
    markup.add(phone_button)

    bot.send_message(
        message.chat.id,
        f"👋 Welcome, {first_name}! \nSend a YouTube, Instagram, or LinkedIn video link to download. 📱 Share your contact for complete registration (optional).",
        reply_markup=markup
    )

@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    if message.contact:
        # Since you are not storing user information in a DB anymore, you can ignore storing the phone number
        bot.reply_to(message, "✅ Thank you! You can now send video links for download!")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    url = message.text.strip()

    if not (url.startswith("http://") or url.startswith("https://")):
        bot.reply_to(message, "❌ Please send a valid link.")
        return

    bot.reply_to(message, "⏳ Processing your request...")
    try:
        file_path = download_media(url)

        if os.path.getsize(file_path) > 50 * 1024 * 1024:
            bot.reply_to(message, "❌ File size exceeds the 50 MB limit.")
            os.remove(file_path)
            return

        with open(file_path, 'rb') as file:
            bot.send_document(message.chat.id, file)

        bot.reply_to(message, "✅ Done! Here's your file.")
        os.remove(file_path)
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

def download_media(url):
    try:
        for file in os.listdir():
            if file.startswith('downloaded_video'):
                os.remove(file)

        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.%(ext)s',
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        downloaded_file = 'downloaded_video.mp4'
        if not os.path.exists(downloaded_file):
            raise Exception("Downloaded video file does not exist.")

        return downloaded_file

    except Exception as e:
        raise Exception(f"Error downloading video: {e}")

logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)

bot.polling(non_stop=True)
