import src.connect_database.connection as co
import sqlite3


class LoginModel:
    def __init__(self):
        self.conn = co.Connection()

    def validate(self, nome, senha):
        try:
            self.conn.connectDB()
            dados = self.conn.cursor.execute("""
                SELECT cpf, nome FROM usuario WHERE nome = ? AND senha = ?
            """, (nome, senha)).fetchall()
            self.conn.desconectDB()
            if dados != []:
                return True
            else:
                return False
        except:
            return False


