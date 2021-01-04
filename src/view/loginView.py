import src.view.templateWindow as tw
import tkinter as tk

import src.controller.loginController as lc


class LoginView(tw.TemplateWindow):
    def __init__(self):
        self.root = tk.Tk()
        # Configurações da Janela
        super().__init__(self.root, 'Gerenciador de Senhas', size='350x200', minx=350, miny=200)

        self.labels()
        self.entrys()
        self.buttons()

        self.lgc = lc.LoginController()

    def start(self):
        self.root.mainloop()

    def labels(self):
        self.lbl_nome_login = tk.Label(self.fra_root, text='Nome:')
        self.lbl_senha_login = tk.Label(self.fra_root, text='Senha')

        self.lbl_nome_login.place(relx=0.20, rely=0.10)
        self.lbl_senha_login.place(relx=0.20, rely=0.40)

    def entrys(self):
        self.ent_nome_login = tk.Entry(self.fra_root)
        self.ent_senha_login = tk.Entry(self.fra_root, show='*')

        self.ent_nome_login.place(relx=0.20, rely=0.20, relwidth=0.60, relheight=0.15)
        self.ent_senha_login.place(relx=0.20, rely=0.50, relwidth=0.60, relheight=0.15)

    def buttons(self):
        self.btn_entrar_login = tk.Button(self.fra_root, text='Entrar')
        self.btn_sair_login = tk.Button(self.fra_root, text='Sair')

        self.btn_entrar_login.place(relx=0.20, rely=0.70, relwidth=0.30, relheight=0.15)
        self.btn_sair_login.place(relx=0.50, rely=0.70, relwidth=0.30, relheight=0.15)

        self.btn_entrar_login['command'] = self.verify
        self.btn_sair_login['command'] = self.quit

    def getEntryLogin(self):
        self.nome_login = str(self.ent_nome_login.get()).strip()
        self.senha_login = str(self.ent_senha_login.get()).strip()

        if self.nome_login != '' and self.senha_login != '':
            return True
        else:
            return False

    def verify(self):
        x = self.getEntryLogin()

        if x:
            # Chamar a função para validar os dados
            ret = self.lgc.validateAccess(self.nome_login, self.senha_login)

            if ret:
                # Fecha a janela e depois chama a tela principal do sistema
                self.quit()
                self.lgc.mainWindow()
            else:
                self.popup(tip=3, tit='ERRO', msg='Dados incorretos.')
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Preencha os campos Nome e Senha.')