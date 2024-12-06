import os
import socks
from telegram.ext import CallbackQueryHandler
from telegram import Update
from telegram.ext import (
    CommandHandler,
    MessageHandler,
    Application,
    filters,
)
from gemini_pro_bot.filters import AuthFilter, MessageFilter, PhotoFilter
from dotenv import load_dotenv
from gemini_pro_bot.handlers import (
    start,
    help_command,
    new_chat,
    handle_message,
    handle_any_file,
    set_model_buttons,
    handle_model_selection,
    show_db_command

)


load_dotenv()

# Proxy settings (replace with your proxy details)
PROXY_HOST = "172.252.110.215"  # Example: "192.168.1.10"
PROXY_PORT = 64676  # Example port
PROXY_TYPE = socks.HTTP  # Or socks.SOCKS4, socks.HTTP, etc.
# You might also need username and password for some proxies:
PROXY_USERNAME = "TQDcLFzD"  # (Optional)
PROXY_PASSWORD = "beBUzDkf"  # (Optional)

# Request kwargs for proxy (create a separate function for reusability)
def request_kwargs(proxy_url=None):
    if proxy_url:
        return {
            "proxy_url": proxy_url,
            "urllib3_proxy_kwargs": {
                "username": PROXY_USERNAME, # Include if your proxy requires it
                "password": PROXY_PASSWORD, # Include if your proxy requires it
            }
        }
    return None

def start_bot() -> None:

    proxy_url = f"http://{PROXY_USERNAME}:{PROXY_PASSWORD}@{PROXY_HOST}:{PROXY_PORT}"


    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder()\
        .token(os.getenv("BOT_TOKEN"))\
            .proxy_url(proxy_url)\
                .build()


    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start, filters=AuthFilter))
    application.add_handler(CommandHandler("help", help_command, filters=AuthFilter))
    application.add_handler(CommandHandler("new", new_chat, filters=AuthFilter))
    application.add_handler(CommandHandler("set_model", set_model_buttons)) # Command to show buttons
    application.add_handler(CallbackQueryHandler(handle_model_selection, pattern="^set_model:"))  # Handler for button presses
    application.add_handler(CommandHandler("show_db", show_db_command))

    # Any text message is sent to LLM to generate a response
    application.add_handler(MessageHandler(MessageFilter, handle_message))

    application.add_handler(MessageHandler(filters.PHOTO, handle_any_file))

    application.add_handler(MessageHandler(filters.Document.ALL, handle_any_file)) # Handles all document types

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
