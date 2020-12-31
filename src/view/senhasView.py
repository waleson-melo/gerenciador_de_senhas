import src.view.templateWindow as tw
import tkinter as tk
import tkinter.ttk as ttk


class SenhasView(tw.TemplateWindow):
    def __init__(self):
        self.root = tk.Tk()
        # Configurações da Janela
        super().__init__(self.root, 'Senhas', menu=True)

        self.framesWindow()
        self.labels()
        self.entrys()
        self.buttons()
        self.lists()

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

    # Labels da Janela
    def labels(self):
        # Aba 1 Senhas
        self.lbl_nome = tk.Label(self.fra_top_senha, text='Nome (App, Site, Banco):')
        self.lbl_tipo = tk.Label(self.fra_top_senha, text='Tipo:')
        self.lbl_login = tk.Label(self.fra_top_senha, text='Login:')
        self.lbl_senha = tk.Label(self.fra_top_senha, text='Senha:')
        self.lbl_observacao = tk.Label(self.fra_top_senha, text='Observação:')

        self.lbl_nome.place(relx=0.05, rely=0.05)
        self.lbl_tipo.place(relx=0.41, rely=0.05)
        self.lbl_login.place(relx=0.05, rely=0.32)
        self.lbl_senha.place(relx=0.41, rely=0.32)
        self.lbl_observacao.place(relx=0.05, rely=0.59)

    # Entrys da Janela
    def entrys(self):
        # Aba 1 Senhas
        self.ent_nome = tk.Entry(self.fra_top_senha)
        # Combobox
        self.tip_var = tk.StringVar(self.fra_top_senha)
        self.tup_tipo = ("App", "Site", "Banco", "Outro")
        self.tip_var.set("App")
        self.opt_tipo = tk.OptionMenu(self.fra_top_senha, self.tip_var, *self.tup_tipo)

        self.ent_login = tk.Entry(self.fra_top_senha)
        self.ent_senha = tk.Entry(self.fra_top_senha)
        self.ent_observacao = tk.Text(self.fra_top_senha)

        self.ent_nome.place(relx=0.05, rely=0.16, relwidth=0.34, relheight=0.14)
        self.opt_tipo.place(relx=0.41, rely=0.16, relwidth=0.34, relheight=0.14)
        self.ent_login.place(relx=0.05, rely=0.43, relwidth=0.34, relheight=0.14)
        self.ent_senha.place(relx=0.41, rely=0.43, relwidth=0.34, relheight=0.14)
        self.ent_observacao.place(relx=0.05, rely=0.70, relwidth=0.7, relheight=0.3)

    # Buttons da Janela
    def buttons(self):
        # Aba 1 Senhas
        self.btn_salvar_senha = tk.Button(self.fra_top_senha, text='Salvar', bd=3)
        self.btn_alterar_senha = tk.Button(self.fra_top_senha, text='Alterar', bd=3)
        self.btn_pesquisar_senha = tk.Button(self.fra_top_senha, text='Pesquisar', bd=3)
        self.btn_apagar_senha = tk.Button(self.fra_top_senha, text='Apagar', bd=3)

        self.btn_salvar_senha.place(relx=0.78, rely=0.16, relwidth=0.18, relheight=0.21)
        self.btn_alterar_senha.place(relx=0.78, rely=0.37, relwidth=0.18, relheight=0.21)
        self.btn_pesquisar_senha.place(relx=0.78, rely=0.58, relwidth=0.18, relheight=0.21)
        self.btn_apagar_senha.place(relx=0.78, rely=0.79, relwidth=0.18, relheight=0.21)

    # Lista da Janela
    def lists(self):
        # Lista de Senhas
        self.trv_senhas = ttk.Treeview(self.fra_bottom_senha, height=3, column=(
            'col1', 'col2', 'col3', 'col4', 'col5', 'col6'))
        self.trv_senhas.heading('#0', text='')
        self.trv_senhas.heading('#1', text='Cod.')
        self.trv_senhas.heading('#2', text='Tipo')
        self.trv_senhas.heading('#3', text='Nome')
        self.trv_senhas.heading('#4', text='Login')
        self.trv_senhas.heading('#5', text='Senha')
        self.trv_senhas.heading('#6', text='Obs.')

        self.trv_senhas.column('#0', width=1)
        self.trv_senhas.column('#1', width=15)
        self.trv_senhas.column('#2', width=15)
        self.trv_senhas.column('#3', width=90)
        self.trv_senhas.column('#4', width=80)
        self.trv_senhas.column('#5', width=80)
        self.trv_senhas.column('#6', width=85)

        self.trv_senhas.place(relx=0.00, rely=0.00, relwidth=0.96, relheight=0.99)