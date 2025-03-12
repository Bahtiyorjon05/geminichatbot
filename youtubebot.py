
# you tube downloader bot

##########################################33

import os
import re
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from yt_dlp import YoutubeDL

# Replace this with your actual Telegram Bot API token
BOT_TOKEN = "8112623211:AAHa9qAsmS8c3TiW-tw3M_CVmKQqk--hvOs"

def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message and usage instructions."""
    update.message.reply_text(
        "Assalomu alaykum va rohmatulloh! 😊\n"
        "Send me a YouTube link, and I will download the video and send it to you."
    )

def is_valid_youtube_url(url: str) -> bool:
    """Check if the URL is a valid YouTube link."""
    youtube_regex = (
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.*'
    )
    return re.match(youtube_regex, url) is not None

def download_video(update: Update, context: CallbackContext) -> None:
    """Download a YouTube video and send it to the user."""
    url = update.message.text

    if not is_valid_youtube_url(url):
        update.message.reply_text("❌ Please send a valid YouTube link!")
        return

    try:
        # Inform the user about the download process
        update.message.reply_text("⏳ Downloading the video... Please wait.")
        
        # yt-dlp options
        options = {
            'format': 'mp4',
            'outtmpl': 'video.mp4',
            'quiet': True,
        }

        with YoutubeDL(options) as ydl:
            ydl.download([url])  # Download the video

        # Check the file size to ensure it's within Telegram's 50MB limit
        file_size = os.path.getsize("video.mp4")
        if file_size > 50 * 1024 * 1024:  # 50MB limit
            update.message.reply_text("❌ This video is too large to send via Telegram (over 50MB).")
            os.remove("video.mp4")  # Clean up the file
            return

        # Send the video to the user
        with open("video.mp4", "rb") as video_file:
            context.bot.send_video(chat_id=update.effective_chat.id, video=video_file)

        update.message.reply_text("✅ Here is your video!")
        os.remove("video.mp4")  # Clean up the file after sending

    except Exception as e:
        # Handle any errors gracefully
        update.message.reply_text(f"❌ An error occurred: {e}")
        if os.path.exists("video.mp4"):
            os.remove("video.mp4")  # Clean up if something goes wrong

def main():
    """Run the bot."""
    # Initialize the Updater and Dispatcher
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command and message handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, download_video))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
