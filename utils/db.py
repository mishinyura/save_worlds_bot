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

    def get_speaker(self, user_id: int) -> list:
        response = self.cursor.execute(
            'SELECT sp.`id`, sp.`name` FROM `users` as us '
            'JOIN `speakers` as sp ON sp.`id` = us.`speaker_voice` WHERE us.`tg_id` = ?',
            [user_id]
        )
        return response.fetchone()

    def speaker_exists(self, speaker_id: int) -> bool:
        response = self.cursor.execute(
            'SELECT `name` FROM `speakers` WHERE `id` = ?',
            [speaker_id]
        )
        return bool(len(response.fetchall()))

    def edit_speaker(self, user_id: int) -> None:
        speaker = self.get_speaker(user_id)
        if self.speaker_exists(speaker[0] + 1):
            new_speaker = speaker[0] + 1
        else:
            new_speaker = 1
        self.cursor.execute(
            'UPDATE `users` SET `speaker_voice` = ? WHERE `tg_id` = ?',
            [new_speaker, user_id]
        )
        self.conn.commit()
        return self.get_speaker(user_id)[1]

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

    def add_remember_word(self, user_id: int, word_id: int) -> None:
        pass