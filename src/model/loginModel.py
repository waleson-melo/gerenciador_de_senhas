import src.connect_database.connection as co
import sqlite3


class LoginModel:
    def __init__(self):
        self.conn = co.Connection()

    def validate(self, cpf, senha):
        print("validando, cpf: {}, senha: {}".format(cpf, senha))
        return True


