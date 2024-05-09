from utils.db import SessionDB
from utils.files import get_path_voice
from loader import bot
import json
from keyboards.inline.change_voice import change_voice_btn

@bot.callback_query_handler(func=lambda call: call.data == 'remembered_word')
def remembered_word_handler(call):
    print(call)


@bot.callback_query_handler(func=lambda call: call.data == 'more_translate')
def more_translate_handler(call):
    print(call)


@bot.callback_query_handler(func=lambda call: json.loads(call.data)['name'] == 'change_voice')
def change_voice_handler(call):
    data = json.loads(call.data)
    db = SessionDB('./database/database.db')
    db.edit_speaker(call.from_user.id)
    db.close_db()
    voice = open(get_path_voice(call.from_user.id, data['audio']), 'rb')
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.send_voice(call.message.chat.id, voice, reply_markup=change_voice_btn(data['audio']))
    voice.close()