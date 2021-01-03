import sqlite3


class Connection:
    def __init__(self):
        self.createTables()

    def connectDB(self):
        self.conn = sqlite3.connect('data_base/dbsistema.db')
        self.cursor = self.conn.cursor()

    def desconectDB(self):
        self.conn.commit()
        self.cursor.close()

    def createTables(self):
        self.connectDB()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "senhas" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "nome"	TEXT NOT NULL,
                "tipo"	TEXT NOT NULL,
                "login"	TEXT NOT NULL,
                "senha"	TEXT NOT NULL,
                "observacoes"	TEXT
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS "usuario" (
                "id"	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                "cpf"	TEXT NOT NULL UNIQUE,
                "nome"	TEXT NOT NULL,
                "telefone"	TEXT,
                "senha"	TEXT NOT NULL
            );
        """)

        self.desconectDB()
