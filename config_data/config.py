import os
from dotenv import load_dotenv, find_dotenv
if not find_dotenv():
    exit("Переменные окружения не загружены, так как отсутствует файл .env")
else:
    load_dotenv()
TOKEN = os.getenv("TOKEN")
DEFAULT_COMMANDS = (
    ('start', 'Запускает бота'),
    ('help', 'Выводит справку'),
    ('word', 'Направляет рандомное слово')
)

SPEAKERS = ['Joanna', 'Justin', 'Matthew', 'Joey', 'Kimberly', 'Kendra', 'Salli']

DATABASE_PATH = 'database/database.db'
speaker = ''