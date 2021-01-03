import src.connect_database.connection as co
import sqlite3


class UsuarioModel:
    def __init__(self):
        self.conn = co.Connection()

    def selectAll(self):
        try:
            self.conn.connectDB()
            dados = self.conn.cursor.execute("""
                SELECT id, cpf, nome, telefone, senha FROM usuario ORDER BY nome ASC
            """).fetchall()
            self.conn.desconectDB()
            return dados
        except sqlite3.Error as erro:
            print(erro)

        return []

    def select(self, cpf):
        ret = None
        try:
            self.conn.connectDB()
            dado = self.conn.cursor.execute("""
                SELECT id, cpf, nome, telefone, senha FROM usuario WHERE cpf = ? 
            """, (cpf,)).fetchall()
            self.conn.desconectDB()

            if len(dado) != 0:
                ret = dado
            else:
                pass
        except sqlite3.Error as erro:
            pass

        return ret

    def save(self, cpf, nome, telefone, senha):
        try:
            self.conn.connectDB()
            self.conn.cursor.execute("""
                INSERT INTO usuario (cpf, nome, telefone, senha) VALUES (?, ?, ?, ?)
            """, (cpf, nome, telefone, senha))
            self.conn.desconectDB()

            return [True, '']
        except sqlite3.Error as erro:
            return [False, str(erro)]

    def update(self, codigo, cpf, nome, telefone, senha):
        try:
            self.conn.connectDB()
            self.conn.cursor.execute("""
                UPDATE usuario SET cpf = ?, nome = ?, telefone = ?, senha = ? WHERE id = ?
            """, (cpf, nome, telefone, senha, codigo))
            self.conn.desconectDB()

            return [True, '']
        except sqlite3.Error as erro:
            return [False, str(erro)]

    def delete(self, codigo):
        try:
            self.conn.connectDB()
            self.conn.cursor.execute("""
                DELETE FROM usuario WHERE id = ?
            """, (codigo,))
            self.conn.desconectDB()

            return [True, '']
        except sqlite3.Error as erro:
            return [False, str(erro)]
