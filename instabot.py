



import telebot
import yt_dlp
import os

# Replace with your bot token from BotFather
BOT_TOKEN = '7665537600:AAHggN60xuyzXP2gO_Us1Yg18IoDOLHa-6s'
bot = telebot.TeleBot(BOT_TOKEN)

# Function to download video using yt_dlp
def download_video(url):
    try:
        # Options for yt_dlp
        ydl_opts = {
            'format': 'best',
            'outtmpl': 'downloaded_video.mp4',  # Save the file locally
            'quiet': True,  # Suppress unnecessary logs
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video
        return 'downloaded_video.mp4'
    except Exception as e:
        raise Exception(f"Failed to download video: {e}")

# Start command handler
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Welcome! 👋 Send me a video link, and I'll download it for you.")

# Message handler for video links
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    url = message.text.strip()

    # Reply if the URL seems invalid
    if not (url.startswith("http://") or url.startswith("https://")):
        bot.reply_to(message, "❌ Please send a valid video link.")
        return

    bot.reply_to(message, "⏳ Processing your request... Please wait.")

    try:
        # Download the video
        file_path = download_video(url)

        # Check file size (Telegram limit: 50 MB for free accounts)
        if os.path.getsize(file_path) > 50 * 1024 * 1024:
            bot.reply_to(message, "❌ Video is too large for Telegram. Try a smaller video.")
            os.remove(file_path)  # Clean up the file
            return

        # Send the video to the user
        with open(file_path, 'rb') as video:
            bot.send_video(message.chat.id, video)

        bot.reply_to(message, "✅ Done! Here's your video.")
        os.remove(file_path)  # Clean up the file after sending

    except Exception as e:
        bot.reply_to(message, f"❌ An error occurred: {str(e)}")

# Start the bot
bot.polling()
