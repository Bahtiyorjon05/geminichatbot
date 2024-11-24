

# import telebot
# from pytube import YouTube

# # Replace with your bot token from BotFather
# BOT_TOKEN = '7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw'

# bot = telebot.TeleBot(BOT_TOKEN)

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.reply_to(message, "Welcome! 👋 Send me a YouTube link, and I'll download it for you (videos up to 50 MB).")

# @bot.message_handler(func=lambda message: True)
# def download_video(message):
#     try:
#         # Extract the URL
#         url = message.text.strip()
        
#         # Validate YouTube link
#         if "youtube.com" not in url and "youtu.be" not in url:
#             bot.reply_to(message, "❌ Please send a valid YouTube link.")
#             return

#         bot.reply_to(message, "⏳ Processing your request. Please wait...")

#         # Download video
#         yt = YouTube(url)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        
#         # Check file size
#         if stream.filesize > 50 * 1024 * 1024:  # 50 MB limit
#             bot.reply_to(message, "❌ Sorry, this video is too large for Telegram. Try a shorter video.")
#             return

#         file_path = stream.download()

#         # Send video
#         with open(file_path, 'rb') as video:
#             bot.send_video(message.chat.id, video)

#         bot.reply_to(message, "✅ Done! Here’s your video. 😊")
#     except Exception as e:
#         bot.reply_to(message, f"❌ An error occurred: {str(e)}")

# bot.polling()



import telebot
import yt_dlp
import os

# Replace with your bot token from BotFather
BOT_TOKEN = '7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw'

bot = telebot.TeleBot(BOT_TOKEN)

# Function to download YouTube video using yt-dlp
def download_youtube_video(url):
    try:
        ydl_opts = {
            'format': 'best[ext=mp4]',  # Choose the best MP4 format
            'outtmpl': '%(title)s.%(ext)s',  # Save file with video title
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)
            return file_name  # Return the downloaded file path
    except Exception as e:
        raise Exception(f"Failed to download video: {e}")

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Welcome! 👋 Send me a YouTube link, and I'll download it for you (videos up to 50 MB).")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text.strip()

    # Validate URL
    if not ("youtube.com" in url or "youtu.be" in url):
        bot.reply_to(message, "❌ Please send a valid YouTube link.")
        return

    bot.reply_to(message, "⏳ Processing your request. Please wait...")

    try:
        # Download video
        file_path = download_youtube_video(url)

        # Check file size (Telegram has a 50 MB limit for non-premium users)
        if os.path.getsize(file_path) > 50 * 1024 * 1024:
            bot.reply_to(message, "❌ Sorry, this video is too large for Telegram. Try a shorter video.")
            os.remove(file_path)  # Clean up the file
            return

        # Send video
        with open(file_path, 'rb') as video:
            bot.send_video(message.chat.id, video)

        bot.reply_to(message, "✅ Done! Here's your video. 😊")
        os.remove(file_path)  # Clean up the file after sending

    except Exception as e:
        bot.reply_to(message, f"❌ An error occurred: {str(e)}")

bot.polling()
