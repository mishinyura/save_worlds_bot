from utils.db import SessionDB
from config_data.config import DATABASE_PATH

def get_path_voice(user_id: int, file_id: int):
    db = SessionDB(DATABASE_PATH)
    speaker = db.get_speaker(user_id)[1]
    path = f'./media/{file_id}-{speaker}.mp3'
    db.close_db()
    return path
