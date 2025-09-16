import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor(buffered=True)
        try:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Error as e:
            print(f"Erro ao executar query: {e}")
            return None

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
