import src.view.senhasView as sv
import src.model.usuarioModel as um


class UsuarioController:
    def __init__(self):
        self.usuario_model = um.UsuarioModel()

    def searchAllUsuarios(self):
        return self.usuario_model.selectAll()

    def searchUsuario(self, cpf):
        return self.usuario_model.select(cpf)

    def saveUsuario(self, cpf, nome, telefone, senha):
        return self.usuario_model.save(cpf, nome, telefone, senha)

    def updateUsuario(self, codigo, cpf, nome, telefone, senha):
        return self.usuario_model.update(codigo, cpf, nome, telefone, senha)

    def deleteUsuario(self, codigo):
        return self.usuario_model.delete(codigo)
