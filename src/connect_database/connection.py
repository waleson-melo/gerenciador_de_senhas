import sqlite3
import os


class Connection:
    def __init__(self):
        self.createTables()

    def connectDB(self):
        if not os.path.isdir(".gerenciador_de_senha/data_base"):
            os.makedirs(".gerenciador_de_senha/data_base")
        self.conn = sqlite3.connect(".gerenciador_de_senha/data_base/dbsistema.db")
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
                "observacao"	TEXT
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

        # se a quantidade for 0 é adcionado um usuario padrao
        quant_usuario = self.cursor.execute("""
            SELECT count(1) FROM usuario
        """).fetchall()
        quant_usuario = list(quant_usuario)[0]
        if quant_usuario[0] == 0:
            self.cursor.execute("""
                INSERT INTO usuario (cpf, nome, senha) VALUES ('00000000000', 'admin', 'admin')
            """)
        self.desconectDB()
