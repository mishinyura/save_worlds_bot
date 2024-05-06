from telebot.types import Message
import random
from utils.db import SessionDB
from loader import bot


@bot.message_handler(commands=["word"])
def bot_word(message: Message):
    word_id = random.randint(1, 19000)
    db = SessionDB('./database/database.db')
    word = db.get_word(word_id)
    db.close_db()
    bot.reply_to(message, '{0} - {1} - {2}'.format(
        word['eng'],
        word['rus'],
        word['transcription']
    ))
    joanna_voice = open(f'./media/{word['audio']}-Joanna.mp3', 'rb')
    justin_voice = open(f'./media/{word['audio']}-Justin.mp3', 'rb')
    matthew_voice = open(f'./media/{word['audio']}-Matthew.mp3', 'rb')
    bot.send_voice(message.chat.id, joanna_voice)
    bot.send_voice(message.chat.id, justin_voice)
    bot.send_voice(message.chat.id, matthew_voice)
    joanna_voice.close()
    justin_voice.close()
    matthew_voice.close()