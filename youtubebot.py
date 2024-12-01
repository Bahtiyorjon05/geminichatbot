




from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import yt_dlp
import os

# Define the start command handler
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! I can help you download YouTube videos. Send me a link.")

# Define the function to handle YouTube video download
async def download_video(update: Update, context: CallbackContext):
    video_url = update.message.text
    if 'youtube.com' in video_url or 'youtu.be' in video_url:
        await update.message.reply_text("Downloading video... please wait.")
        
        # Define the download options
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',  # Saves in 'downloads' folder
            'quiet': True,  # Suppress unnecessary output
        }
        
        # Perform the download using yt-dlp
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=True)
                video_title = info_dict.get('title', None)
                video_file = f"downloads/{video_title}.mp4"
                
                # Send the video back to the user
                if os.path.exists(video_file):
                    with open(video_file, 'rb') as video:
                        await update.message.reply_video(video, caption=f"Here is your video: {video_title}")
                    os.remove(video_file)  # Clean up after sending the video
                else:
                    await update.message.reply_text("There was an issue downloading the video.")
        except Exception as e:
            await update.message.reply_text(f"Error: {e}")
    else:
        await update.message.reply_text("Please send a valid YouTube video link.")

# Define the main function to start the bot
def start_bot():
    # Initialize the Application with your bot token
    application = Application.builder().token("7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw").build()

    # Add command handler for the '/start' command
    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    # Add message handler to handle YouTube video links
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, download_video)
    application.add_handler(message_handler)

    # Start the bot and handle polling
    application.run_polling()

if __name__ == "__main__":
    start_bot()



































# import telebot
# import yt_dlp
# import os

# # Load bot token from environment
# BOT_TOKEN = os.getenv('BOT_TOKEN', '7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw')
# bot = telebot.TeleBot(BOT_TOKEN)

# # Function to download YouTube video and save as a file
# def download_youtube_video(url):
#     try:
#         # Fetch video metadata
#         ydl_opts_info = {
#             'quiet': True,
#             'cookies': 'cookies.txt'  # Use cookies for authentication
#         }
#         with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
#             info_dict = ydl.extract_info(url, download=False)
#             file_size = info_dict.get('filesize', 0)

#             # Check file size limit
#             if file_size and file_size > 50 * 1024 * 1024:
#                 raise Exception("Video exceeds the 50 MB Telegram limit.")
        
#         # Download the video in MP4 format
#         ydl_opts = {
#     'format': 'best[ext=mp4]',
#     'outtmpl': 'downloaded_video.mp4',
#     'quiet': True,
#     'cookiefile': 'path_to_your_cookies_file.txt',  # Add this line to load cookies
# }

#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         return 'downloaded_video.mp4'
#     except Exception as e:
#         raise Exception(f"Failed to download video: {e}")

# # Start command
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.reply_to(message, "Welcome! 👋 Send me a YouTube link, and I'll download it for you.")

# # Handle YouTube links
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     url = message.text.strip()

#     # Validate YouTube URL
#     if not ("youtube.com" in url or "youtu.be" in url):
#         bot.reply_to(message, "❌ Please send a valid YouTube link.")
#         return

#     bot.reply_to(message, "⏳ Processing your request... Please wait.")

#     try:
#         # Download video
#         file_path = download_youtube_video(url)

#         # Send the video
#         with open(file_path, 'rb') as video:
#             bot.send_video(message.chat.id, video)

#         bot.reply_to(message, "✅ Done! Here's your video.")
#         os.remove(file_path)  # Clean up the downloaded file

#     except Exception as e:
#         bot.reply_to(message, f"❌ An error occurred: {str(e)}")

# # Start bot polling
# bot.polling()














# import telebot
# import yt_dlp
# import os

# # Load bot token from environment
# BOT_TOKEN = os.getenv('BOT_TOKEN', '7049015817:AAGZbrdOhD14xjyO1xDYdQiwvdR9RNZuLkw')
# bot = telebot.TeleBot(BOT_TOKEN)

# # Function to download YouTube video and save as a file
# def download_youtube_video(url):
#     try:
#         # Fetch video metadata
#         ydl_opts_info = {'quiet': True}
#         with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
#             info_dict = ydl.extract_info(url, download=False)
#             file_size = info_dict.get('filesize', 0)

#             # Check file size limit
#             if file_size > 50 * 1024 * 1024:
#                 raise Exception("Video exceeds the 50 MB Telegram limit.")
        
#         # Download the video in MP4 format
#         ydl_opts = {
#             'format': 'best[ext=mp4]',
#             'outtmpl': 'downloaded_video.mp4',
#             'quiet': True,
#         }
#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])
#         return 'downloaded_video.mp4'
#     except Exception as e:
#         raise Exception(f"Failed to download video: {e}")

# # Start command
# @bot.message_handler(commands=['start'])
# def welcome(message):
#     bot.reply_to(message, "Welcome! 👋 Send me a YouTube link, and I'll download it for you.")

# # Handle YouTube links
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     url = message.text.strip()

#     # Validate YouTube URL
#     if not ("youtube.com" in url or "youtu.be" in url):
#         bot.reply_to(message, "❌ Please send a valid YouTube link.")
#         return

#     bot.reply_to(message, "⏳ Processing your request... Please wait.")

#     try:
#         # Download video
#         file_path = download_youtube_video(url)

#         # Send the video
#         with open(file_path, 'rb') as video:
#             bot.send_video(message.chat.id, video)

#         bot.reply_to(message, "✅ Done! Here's your video.")
#         os.remove(file_path)  # Clean up the downloaded file

#     except Exception as e:
#         bot.reply_to(message, f"❌ An error occurred: {str(e)}")

# # Start bot polling
# bot.polling()




















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
