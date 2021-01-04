import src.view.loginView as lv
import src.model.loginModel as lm
import src.controller.mainWindowController as mc


class LoginController:
    def __init__(self):
        self.lgm = lm.LoginModel()

    def run(self):
        self.lgv = lv.LoginView()
        self.lgv.start()

    def validateAccess(self, nome, senha):
        return self.lgm.validate(nome, senha)

    def mainWindow(self):
        self.mnc = mc.MainWindowController()
        self.mnc.run()