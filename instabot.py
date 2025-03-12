

# #    instagram  you tube linkedin video download bot

# import telebot
# import yt_dlp
# import os
# import sqlite3
# import time
# import logging
# from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# from flask import Flask
# import threading

# # Bot token from BotFather
# BOT_TOKEN = '7665537600:AAHggN60xuyzXP2gO_Us1Yg18IoDOLHa-6s'
# bot = telebot.TeleBot(BOT_TOKEN)

# # Database setup
# DB_FILE = 'bot_users.db'

# def init_db():
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 username TEXT,
#                 first_name TEXT,
#                 last_name TEXT,
#                 phone_number TEXT DEFAULT 'Not Provided',
#                 videos_downloaded INTEGER DEFAULT 0,
#                 start_time TEXT DEFAULT CURRENT_TIMESTAMP
#             )
#         ''')
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS downloads (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 user_id INTEGER,
#                 video_url TEXT,
#                 download_time TEXT DEFAULT CURRENT_TIMESTAMP,
#                 FOREIGN KEY (user_id) REFERENCES users (id)
#             )
#         ''')
#         conn.commit()

# def register_user(user_id, username, first_name, last_name, phone_number):
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('SELECT 1 FROM users WHERE id = ?', (user_id,))
#         if not cursor.fetchone():
#             start_time = time.strftime('%Y-%m-%d %H:%M:%S')
#             cursor.execute(''' 
#                 INSERT INTO users (id, username, first_name, last_name, phone_number, start_time) 
#                 VALUES (?, ?, ?, ?, ?, ?)
#             ''', (user_id, username, first_name, last_name, phone_number, start_time))
#             conn.commit()

# def increment_video_downloads(user_id):
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         cursor.execute('UPDATE users SET videos_downloaded = videos_downloaded + 1 WHERE id = ?', (user_id,))
#         conn.commit()

# def log_download(user_id, video_url):
#     with sqlite3.connect(DB_FILE) as conn:
#         cursor = conn.cursor()
#         download_time = time.strftime('%Y-%m-%d %H:%M:%S')
#         cursor.execute(''' 
#             INSERT INTO downloads (user_id, video_url, download_time) 
#             VALUES (?, ?, ?)
#         ''', (user_id, video_url, download_time))
#         conn.commit()

# def download_media(url):
#     try:
#         for file in os.listdir():
#             if file.startswith('downloaded_video'):
#                 os.remove(file)

#         ydl_opts = {
#             'format': 'best',
#             'outtmpl': 'downloaded_video.%(ext)s',
#             'quiet': True,
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#         downloaded_file = 'downloaded_video.mp4'
#         if not os.path.exists(downloaded_file):
#             raise Exception("Downloaded video file does not exist.")

#         return downloaded_file

#     except Exception as e:
#         raise Exception(f"Error downloading video: {e}")

# # Flask Setup
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Your bot is running! 📱"

# def run_flask():
#     app.run(host="0.0.0.0", port=3000)

# # Start Flask in a separate thread
# flask_thread = threading.Thread(target=run_flask)
# flask_thread.start()

# # Bot Handlers
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     user_id = message.from_user.id
#     username = message.from_user.username or "unknown"
#     first_name = message.from_user.first_name or "Unknown"
#     last_name = message.from_user.last_name or "Unknown"
#     register_user(user_id, username, first_name, last_name, "Not Provided")

#     markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     phone_button = KeyboardButton("📱 Share Contact", request_contact=True)
#     markup.add(phone_button)

#     bot.send_message(
#         message.chat.id,
#         f"👋 Welcome, {first_name}! \nSend a YouTube, Instagram, or LinkedIn video link to download. 📱 Share your contact for complete registration (optional).",
#         reply_markup=markup
#     )

# @bot.message_handler(content_types=['contact'])
# def handle_contact(message):
#     if message.contact:
#         user_id = message.contact.user_id
#         phone_number = message.contact.phone_number

#         with sqlite3.connect(DB_FILE) as conn:
#             cursor = conn.cursor()
#             cursor.execute('UPDATE users SET phone_number = ? WHERE id = ?', (phone_number, user_id))
#             conn.commit()

#         bot.reply_to(message, "✅ Thank you! Your phone number has been saved. You can now send video links for download!")

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     user_id = message.from_user.id
#     url = message.text.strip()

#     if not (url.startswith("http://") or url.startswith("https://")):
#         bot.reply_to(message, "❌ Please send a valid link.")
#         return

#     bot.reply_to(message, "⏳ Processing your request...")
#     try:
#         file_path = download_media(url)

#         if os.path.getsize(file_path) > 50 * 1024 * 1024:
#             bot.reply_to(message, "❌ File size exceeds the 50 MB limit.")
#             os.remove(file_path)
#             return

#         with open(file_path, 'rb') as file:
#             bot.send_document(message.chat.id, file)

#         increment_video_downloads(user_id)  # Increment video count for the user
#         log_download(user_id, url)  # Log the download in the database
#         bot.reply_to(message, "✅ Done! Here's your file.")
#         os.remove(file_path)
#     except Exception as e:
#         bot.reply_to(message, f"❌ Error: {str(e)}")

# logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)
# init_db()
# bot.polling(non_stop=True)


###################################################3


import telebot
import yt_dlp
import os
import sqlite3
import time
import logging
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Bot token from BotFather
BOT_TOKEN = '7665537600:AAHggN60xuyzXP2gO_Us1Yg18IoDOLHa-6s'
bot = telebot.TeleBot(BOT_TOKEN)

# Database setup
DB_FILE = 'bot_users.db'

def init_db():
    # Check if the database file exists and create or alter tables if needed
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        
        # Create users table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                first_name TEXT,
                last_name TEXT,
                phone_number TEXT DEFAULT 'Not Provided',
                videos_downloaded INTEGER DEFAULT 0,
                start_time TEXT DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create downloads table with simplified schema
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS downloads (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                video_url TEXT,
                download_time TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        conn.commit()

def register_user(user_id, username, first_name, last_name, phone_number):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1 FROM users WHERE id = ?', (user_id,))
        if not cursor.fetchone():
            start_time = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(''' 
                INSERT INTO users (id, username, first_name, last_name, phone_number, start_time) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (user_id, username, first_name, last_name, phone_number, start_time))
            conn.commit()

def increment_video_downloads(user_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET videos_downloaded = videos_downloaded + 1 WHERE id = ?', (user_id,))
        conn.commit()

def log_download(user_id, video_url):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        download_time = time.strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(''' 
            INSERT INTO downloads (user_id, video_url, download_time) 
            VALUES (?, ?, ?)
        ''', (user_id, video_url, download_time))
        conn.commit()

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
        
        # Return the downloaded file path
        return downloaded_file

    except Exception as e:
        raise Exception(f"Error downloading video: {e}")

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username or "unknown"
    first_name = message.from_user.first_name or "Unknown"
    last_name = message.from_user.last_name or "Unknown"
    register_user(user_id, username, first_name, last_name, "Not Provided")

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
        user_id = message.contact.user_id
        phone_number = message.contact.phone_number

        with sqlite3.connect(DB_FILE) as conn:
            cursor = conn.cursor()
            cursor.execute('UPDATE users SET phone_number = ? WHERE id = ?', (phone_number, user_id))
            conn.commit()

        bot.reply_to(message, "✅ Thank you! Your phone number has been saved. You can now send video links for download!")

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
        
        increment_video_downloads(user_id)  # Increment video count for the user
        log_download(user_id, url)  # Log the download in the database
        bot.reply_to(message, "✅ Done! Here's your file.")
        os.remove(file_path)
    except Exception as e:
        bot.reply_to(message, f"❌ Error: {str(e)}")

logging.basicConfig(filename='bot_errors.log', level=logging.ERROR)
init_db()
bot.polling()




