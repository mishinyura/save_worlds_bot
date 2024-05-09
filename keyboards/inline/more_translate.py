from loader import bot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import json

def word_btn() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton('Помню слово', callback_data='remembered_word'))
    keyboard.add(InlineKeyboardButton('Подробнее о переводе', callback_data='more_translate'))
    return keyboard
