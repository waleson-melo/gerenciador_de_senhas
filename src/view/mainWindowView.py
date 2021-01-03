import tkinter as tk
import tkinter.ttk as ttk

import src.view.templateWindow as tw
import src.view.senhasView as sv


class MainWindowView(tw.TemplateWindow):
    def __init__(self):
        self.root = tk.Tk()
        # Configurações da Janela
        super().__init__(self.root, 'Gerenciador de Senhas', size='750x550',menu=True)

        self.framesWindow() # Cria os Frames

        self.sev = sv.SenhasView(
            self.fra_top_senha, self.fra_top_usuario,
            self.fra_bottom_senha, self.fra_bottom_usuario
        )

        self.labels()       # Cria as Labels
        self.entrys()       # Cria as Entrys
        self.buttons()      # Cria os Buttons
        self.lists()        # Cria a Lista
        self.addDadoList()   # Insere os dados na Lista
        # self.listUsuario()  # Insere os dados na Lista


    def start(self):
        self.root.mainloop()

    # Layout dos frames ta tela
    def framesWindow(self):
        self.abas = ttk.Notebook(self.fra_root)

        self.aba1 = tk.Frame(self.abas)
        self.aba2 = tk.Frame(self.abas)

        self.abas.add(self.aba1, text='Senhas')
        self.abas.add(self.aba2, text='Usuário')

        self.abas.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)

        # Aba 1 Senhas
        self.fra_top_senha = tk.Frame(self.aba1, bd=3)
        # self.fra_top_senha['bg'] = 'blue'
        self.fra_top_senha.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.4)

        self.fra_bottom_senha = tk.Frame(self.aba1)
        # self.fra_top_senha['bg'] = 'blue'
        self.fra_bottom_senha.place(relx=0.00, rely=0.42, relwidth=1.00, relheight=0.6)

        # Aba 2 Usuarios
        self.fra_top_usuario = tk.Frame(self.aba2, bd=3)
        # self.fra_top_senha['bg'] = 'blue'
        self.fra_top_usuario.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.4)

        self.fra_bottom_usuario = tk.Frame(self.aba2)
        # self.fra_top_senha['bg'] = 'blue'
        self.fra_bottom_usuario.place(relx=0.00, rely=0.42, relwidth=1.00, relheight=0.6)

    def labels(self):
        self.sev.labelsSenha()

    def entrys(self):
        self.sev.entrysSenha()

    def buttons(self):
        self.sev.buttonsSenha()

    def lists(self):
        self.sev.listSenha()

    def addDadoList(self):
        self.sev.addSenhaslist()