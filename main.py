from gemini_pro_bot.bot import start_bot
from gemini_pro_bot.handlers import init_db


if __name__ == "__main__":
    init_db()
    start_bot()