import json

from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from utils.db import SessionDB

if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()