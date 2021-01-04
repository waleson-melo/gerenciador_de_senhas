import src.view.templateWindow as tw
import tkinter as tk

import src.controller.loginController as lc


class LoginView(tw.TemplateWindow):
    def __init__(self, root):
        self.root = root
        self.lgc = lc.LoginController()

    def login(self):
        self.window(self.root, name='Entrar no Sistema', size='350x200', closeAll=True)
        self.labels()
        self.entrys()
        self.buttons()

    def labels(self):
        self.lbl_cpf_login = tk.Label(self.fra_root2, text='CPF:')
        self.lbl_senha_login = tk.Label(self.fra_root2, text='Senha')

        self.lbl_cpf_login.place(relx=0.20, rely=0.10)
        self.lbl_senha_login.place(relx=0.20, rely=0.40)

    def entrys(self):
        self.ent_cpf_login = tk.Entry(self.fra_root2)
        self.ent_senha_login = tk.Entry(self.fra_root2, show='*')

        self.ent_cpf_login.place(relx=0.20, rely=0.20, relwidth=0.60, relheight=0.15)
        self.ent_senha_login.place(relx=0.20, rely=0.50, relwidth=0.60, relheight=0.15)

    def buttons(self):
        self.btn_entrar_login = tk.Button(self.fra_root2, text='Entrar')
        self.btn_sair_login = tk.Button(self.fra_root2, text='Sair')

        self.btn_entrar_login.place(relx=0.20, rely=0.70, relwidth=0.30, relheight=0.15)
        self.btn_sair_login.place(relx=0.50, rely=0.70, relwidth=0.30, relheight=0.15)

        self.btn_entrar_login['command'] = self.verify
        self.btn_sair_login['command'] = self.quit

    def getEntryLogin(self):
        self.cpf_login = str(self.ent_cpf_login.get()).strip()
        self.senha_login = str(self.ent_senha_login.get()).strip()

        if self.cpf_login != '' and self.senha_login != '':
            return True
        else:
            return False

    def verify(self):
        x = self.getEntryLogin()

        if x:
            # Chamar a função para validar os dados
            ret = self.lgc.validateAccess(self.cpf_login, self.senha_login)

            if ret:
                self.quitSecundaria()
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Preencha os campos CPF e Senha.')