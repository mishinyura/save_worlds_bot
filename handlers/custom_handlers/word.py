import random
from telebot.types import Message
from loader import bot
from utils.db import SessionDB
from utils.files import get_path_voice
from keyboards.inline.change_voice import change_voice_btn
from keyboards.inline.more_translate import word_btn



@bot.message_handler(commands=["word"])
def bot_word(message: Message):
    word_id = random.randint(1, 19000)
    db = SessionDB('./database/database.db')
    word = db.get_word(word_id)
    db.close_db()
    bot.send_message(
        message.chat.id,
        '\tСлово: *{0}*\nПеревод: ||{1}||\nТранскрипция: {2}'.format(
            word['eng'],
            word['rus'],
            word['transcription']
        ),
        parse_mode='MarkdownV2',
        reply_markup=word_btn()
    )
    voice = open(get_path_voice(message.from_user.id, word['audio']), 'rb')
    bot.send_voice(message.chat.id, voice, reply_markup=change_voice_btn(word['audio']))
    voice.close()