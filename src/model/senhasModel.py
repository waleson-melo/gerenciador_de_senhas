import src.connect_database.connection as co
import sqlite3


class SenhasModel:
    def __init__(self):
        self.conn = co.Connection()

    def selectAll(self):
        try:
            self.conn.connectDB()
            dados = self.conn.cursor.execute("""
                SELECT id, tipo, nome, login, senha, observacao FROM senhas ORDER BY tipo ASC
            """).fetchall()
            self.conn.desconectDB()
            return dados
        except sqlite3.Error as erro:
            print(erro)

        return []

    def select(self, nome):
        ret = None
        try:
            self.conn.connectDB()
            dado = self.conn.cursor.execute("""
                SELECT id, tipo, nome, login, senha, observacao FROM senhas WHERE nome = ? 
            """, (nome,)).fetchall()
            self.conn.desconectDB()

            if len(dado) != 0:
                ret = dado
            else:
                pass
        except sqlite3.Error as erro:
            pass

        return ret

    def save(self, nome, tipo, login, senha, obs):
        try:
            self.conn.connectDB()
            self.conn.cursor.execute("""
                INSERT INTO senhas (nome, tipo, login, senha, observacao) VALUES (?, ?, ?, ?, ?)
            """, (nome, tipo, login, senha, obs))
            self.conn.desconectDB()

            return [True, '']
        except sqlite3.Error as erro:
            return [False, str(erro)]

    def update(self, codigo, nome, tipo, login, senha, obs):
        try:
            self.conn.connectDB()
            self.conn.cursor.execute("""
                UPDATE senhas SET nome = ?, tipo = ?, login = ?, senha = ?, observacao = ? WHERE id = ?
            """, (nome, tipo, login, senha, obs, codigo))
            self.conn.desconectDB()

            return [True, '']
        except sqlite3.Error as erro:
            return [False, str(erro)]

    def delete(self, codigo):
        try:
            self.conn.connectDB()
            self.conn.cursor.execute("""
                DELETE FROM senhas WHERE id = ?
            """, (codigo,))
            self.conn.desconectDB()

            return [True, '']
        except sqlite3.Error as erro:
            return [False, str(erro)]
