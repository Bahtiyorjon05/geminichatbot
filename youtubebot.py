


import telebot
import yt_dlp
import os

# Load bot token from environment
BOT_TOKEN = os.getenv('BOT_TOKEN', '7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw')
bot = telebot.TeleBot(BOT_TOKEN)

# Function to download YouTube video and save as a file
def download_youtube_video(url):
    try:
        # Fetch video metadata
        ydl_opts_info = {'quiet': True}
        with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            file_size = info_dict.get('filesize', 0)

            # Check file size limit
            if file_size > 50 * 1024 * 1024:
                raise Exception("Video exceeds the 50 MB Telegram limit.")
        
        # Download the video in MP4 format
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': 'downloaded_video.mp4',
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return 'downloaded_video.mp4'
    except Exception as e:
        raise Exception(f"Failed to download video: {e}")

# Start command
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Welcome! 👋 Send me a YouTube link, and I'll download it for you.")

# Handle YouTube links
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text.strip()

    # Validate YouTube URL
    if not ("youtube.com" in url or "youtu.be" in url):
        bot.reply_to(message, "❌ Please send a valid YouTube link.")
        return

    bot.reply_to(message, "⏳ Processing your request... Please wait.")

    try:
        # Download video
        file_path = download_youtube_video(url)

        # Send the video
        with open(file_path, 'rb') as video:
            bot.send_video(message.chat.id, video)

        bot.reply_to(message, "✅ Done! Here's your video.")
        os.remove(file_path)  # Clean up the downloaded file

    except Exception as e:
        bot.reply_to(message, f"❌ An error occurred: {str(e)}")

# Start bot polling
bot.polling()




















# import telebot
# import yt_dlp
# import os

# # Replace with your bot token from BotFather
# BOT_TOKEN = '7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw'
# bot = telebot.TeleBot(BOT_TOKEN)

# # Function to download YouTube video and save it as a file
# def download_youtube_video(url):
#     try:
#         # Setting options to download the video in MP4 format
#         ydl_opts = {
#             'format': 'best[ext=mp4]',  # Choose the best MP4 format
#             'outtmpl': 'downloaded_video.mp4',  # Save the video to a local file
#             'quiet': True,  # Suppress unnecessary output
#         }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])  # Download the video
#             return 'downloaded_video.mp4'  # Return the filename
#     except Exception as e:
#         raise Exception(f"Failed to download video: {e}")

# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.reply_to(message, "Welcome! 👋 Send me a YouTube link, and I'll download it for you.")

# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     url = message.text.strip()

#     # Validate YouTube URL
#     if not ("youtube.com" in url or "youtu.be" in url):
#         bot.reply_to(message, "❌ Please send a valid YouTube link.")
#         return

#     bot.reply_to(message, "⏳ Processing your request... Please wait.")

#     try:
#         # Download video and get the filename
#         file_path = download_youtube_video(url)

#         # Check if the video is too large for Telegram (50 MB limit)
#         if os.path.getsize(file_path) > 50 * 1024 * 1024:
#             bot.reply_to(message, "❌ Video is too large for Telegram. Try a shorter video.")
#             os.remove(file_path)  # Clean up the downloaded file
#             return

#         # Send the video
#         with open(file_path, 'rb') as video:
#             bot.send_video(message.chat.id, video)

#         bot.reply_to(message, "✅ Done! Here's your video.")

#         os.remove(file_path)  # Clean up the downloaded file

#     except Exception as e:
#         bot.reply_to(message, f"❌ An error occurred: {str(e)}")

# bot.polling()
