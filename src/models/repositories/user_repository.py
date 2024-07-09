from sqlite3 import Connection

class UserRepository:
    def __init__(self, db_connection: Connection) -> None:
        self.__conn = db_connection

    def registry_user(self, username: str, password: str) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            'INSERT INTO users (username, password, balance) VALUES (?, ?, ?);',
            (username, password, 0)
        )

        self.__conn.commit()

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            'UPDATE users SET balance = ? WHERE id = ?;',
            (new_balance, user_id)
        )

        self.__conn.commit()

    def get_user_by_username(self, username: str) -> tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            'SELECT id, username, password FROM users WHERE username = ?;',
            (username,)
        )

        return cursor.fetchone()
    
    def delete_user_by_id(self, user_id: int) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            'DELETE FROM users WHERE id = ?;',
            (user_id,)
        )

        self.__conn.commit()

