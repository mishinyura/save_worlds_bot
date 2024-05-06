import sqlite3
import datetime
from utils.formatter import format_data_word
class SessionDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cursor = self.conn.cursor()

    def close_db(self):
        self.conn.close()

    def user_exists(self, user_id: int) -> bool:
        """Проверка на существование польователя в БД
        :param user_id: id telegram аккаунта
        """
        response = self.cursor.execute(
            'SELECT `id` FROM `users` WHERE `tg_id` = ?',
            [user_id]
        )
        return bool(len(response.fetchall()))

    def get_user_id(self, user_id: int) -> int:
        response = self.cursor.execute(
            'SELECT `id` FROM `users` WHERE `tg_id` = ?',
            [user_id]
        )
        return response.fetchone()[0]

    def add_user(self, user_id: int, user: str, f_name: str, l_name: str) -> None:
        self.cursor.execute(
            'INSERT INTO '
            '`users` (`tg_id`, `username`, `first_name`, `last_name`, `reg_datetime`) '
            'VALUES (?, ?, ?, ?, ?)',
            [
                user_id,
                user,
                f_name,
                l_name,
                datetime.datetime.now()
            ]
        )
        self.conn.commit()

    def get_word(self, word_id: int):
        response = self.cursor.execute(
            'SELECT * FROM `words` WHERE `id` = ?',
            [word_id]
        )
        data = format_data_word(response.fetchone())
        return data

    def add_word(self, e_word: str, r_word: str, transcription: str):
        self.cursor.execute(
            'INSERT INTO `words` (`eng`, `rus`, `transcription`) VALUES (?, ?, ?)',
            [
                e_word,
                r_word,
                transcription
            ]
        )
        self.conn.commit()

    def update_word(self, word_id: int, col: str, val):
        self.cursor.execute(
            f'UPDATE `words` SET `{col}` = ? WHERE `id` = ?',
            [
                val,
                word_id
            ]
        )
        self.conn.commit()