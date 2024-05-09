from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from loader import bot
import json
from utils.db import SessionDB
from utils.files import get_path_voice

def change_voice_btn(num_audio: int) -> InlineKeyboardMarkup:
    data = {
        'audio': num_audio,
        'name': 'change_voice'
    }
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Сменить голос', callback_data=json.dumps(data)))
    return keyboard