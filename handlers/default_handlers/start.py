from telebot.types import Message
from utils.db import SessionDB
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    print(message)
    db = SessionDB('./database/database.db')
    if not db.user_exists(message.from_user.id):
        db.add_user(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name
        )
    db.close_db()
    if message.from_user.first_name.isalpha():
        name = message.from_user.first_name
    else:
        name = message.from_user.username
    bot.reply_to(message, f"Привет, {name}!")
