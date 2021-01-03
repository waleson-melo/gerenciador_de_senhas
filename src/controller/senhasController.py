import src.view.senhasView as sv
import src.model.senhasModel as sm


class SenhasController:
    def __init__(self):
        self.senhas_model = sm.SenhasModel()

    def start(self):
        sev = sv.SenhasView(self)
        sev.start()

    def searchAllSenhas(self):
        return self.senhas_model.selectAll()

    def searchSenha(self, nome):
        return self.senhas_model.select(nome)

    def saveSenha(self, nome, tipo, login, senha, obs):
        return self.senhas_model.save(nome, tipo, login, senha, obs)

    def updateSenha(self, codigo, nome, tipo, login, senha, obs):
        return self.senhas_model.update(codigo, nome, tipo, login, senha, obs)

    def deleteSenha(self, codigo):
        return self.senhas_model.delete(codigo)
