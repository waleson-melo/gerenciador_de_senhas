import src.view.loginView as lv
import src.model.loginModel as lm


class LoginController:
    def __init__(self):
        self.lgm = lm.LoginModel()

    def validateAccess(self, cpf, senha):
        return self.lgm.validate(cpf, senha)