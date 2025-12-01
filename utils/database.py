import sqlite3


class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_db()

    def create_db(self):
        try:
            query = (
                "CREATE TABLE IF NOT EXISTS USERS("
                "id INTEGER PRIMARY KEY,"
                "user_name TEXT,"
                "user_city TEXT,"
                "telegram_id INTEGER);"
            )
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as Error:
            print("Помилка при створенні:", Error)

    def add_user(self, user_name, user_city, telegram_id):
        self.cursor.execute(
            f"INSERT INTO users (user_name, user_city, telegram_id) VALUES (?,?,?)",
            (user_name, user_city, telegram_id),
        )
        self.connection.commit()

    def select_user_id(self, telegram_id):
        users = self.cursor.execute(
            "SELECT * FROM users WHERE telegram_id = ?", (telegram_id,)
        )
        return users.fetchone()

    def __del__(self):
        self.cursor.close()
        self.connection.close()
