import src.view.templateWindow as tw
import tkinter as tk
import tkinter.ttk as ttk


class SenhasView(tw.TemplateWindow):
    def __init__(self):
        self.root = tk.Tk()
        # Configurações da Janela
        super().__init__(self.root, 'Gerenciador de Senhas', menu=True)

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
        self.lbl_nome_senha = tk.Label(self.fra_top_senha, text='Nome (App, Site, Banco):')
        self.lbl_tipo_senha = tk.Label(self.fra_top_senha, text='Tipo:')
        self.lbl_login_senha = tk.Label(self.fra_top_senha, text='Login:')
        self.lbl_senha_senha = tk.Label(self.fra_top_senha, text='Senha:')
        self.lbl_observacao_senha = tk.Label(self.fra_top_senha, text='Observação:')

        self.lbl_nome_senha.place(relx=0.05, rely=0.05)
        self.lbl_tipo_senha.place(relx=0.41, rely=0.05)
        self.lbl_login_senha.place(relx=0.05, rely=0.32)
        self.lbl_senha_senha.place(relx=0.41, rely=0.32)
        self.lbl_observacao_senha.place(relx=0.05, rely=0.59)

        # Aba 2 Usuario
        self.lbl_cpf_usuario = tk.Label(self.fra_top_usuario, text='CPF:')
        self.lbl_nome_usuario = tk.Label(self.fra_top_usuario, text='Nome:')
        self.lbl_login_usuario = tk.Label(self.fra_top_usuario, text='Login:')
        self.lbl_senha_usuario = tk.Label(self.fra_top_usuario, text='Senha:')

        self.lbl_cpf_usuario.place(relx=0.05, rely=0.05)
        self.lbl_nome_usuario.place(relx=0.41, rely=0.05)
        self.lbl_login_usuario.place(relx=0.05, rely=0.32)
        self.lbl_senha_usuario.place(relx=0.41, rely=0.32)

    # Entrys da Janela
    def entrys(self):
        # Aba 1 Senhas
        self.ent_codigo_senha = tk.Entry(self.fra_top_senha)
        self.ent_nome_senha = tk.Entry(self.fra_top_senha)
        # Combobox
        self.tip_var_senha = tk.StringVar(self.fra_top_senha)
        self.tup_tipo_senha = ("App", "Site", "Banco", "Outro")
        self.tip_var_senha.set("App")
        self.opt_tipo_senha = tk.OptionMenu(self.fra_top_senha, self.tip_var_senha, *self.tup_tipo_senha)

        self.ent_login_senha = tk.Entry(self.fra_top_senha)
        self.ent_senha_senha = tk.Entry(self.fra_top_senha)
        self.ent_observacao_senha = tk.Text(self.fra_top_senha)

        self.ent_nome_senha.place(relx=0.05, rely=0.16, relwidth=0.34, relheight=0.14)
        self.opt_tipo_senha.place(relx=0.41, rely=0.16, relwidth=0.34, relheight=0.14)
        self.ent_login_senha.place(relx=0.05, rely=0.43, relwidth=0.34, relheight=0.14)
        self.ent_senha_senha.place(relx=0.41, rely=0.43, relwidth=0.34, relheight=0.14)
        self.ent_observacao_senha.place(relx=0.05, rely=0.70, relwidth=0.7, relheight=0.3)

        # Aba 2 Usuario
        self.ent_codigo_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_cpf_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_nome_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_login_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_senha_usuario = tk.Entry(self.fra_top_usuario)

        self.ent_cpf_usuario.place(relx=0.05, rely=0.16, relwidth=0.34, relheight=0.14)
        self.ent_nome_usuario.place(relx=0.41, rely=0.16, relwidth=0.34, relheight=0.14)
        self.ent_login_usuario.place(relx=0.05, rely=0.43, relwidth=0.34, relheight=0.14)
        self.ent_senha_usuario.place(relx=0.41, rely=0.43, relwidth=0.34, relheight=0.14)

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

        # Aba 2 Usuario
        self.btn_salvar_usuario = tk.Button(self.fra_top_usuario, text='Salvar', bd=3)
        self.btn_alterar_usuario = tk.Button(self.fra_top_usuario, text='Alterar', bd=3)
        self.btn_pesquisar_usuario = tk.Button(self.fra_top_usuario, text='Pesquisar', bd=3)
        self.btn_apagar_usuario = tk.Button(self.fra_top_usuario, text='Apagar', bd=3)

        self.btn_salvar_usuario.place(relx=0.78, rely=0.16, relwidth=0.18, relheight=0.21)
        self.btn_alterar_usuario.place(relx=0.78, rely=0.37, relwidth=0.18, relheight=0.21)
        self.btn_pesquisar_usuario.place(relx=0.78, rely=0.58, relwidth=0.18, relheight=0.21)
        self.btn_apagar_usuario.place(relx=0.78, rely=0.79, relwidth=0.18, relheight=0.21)

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
        self.trv_senhas.column('#1', width=49)
        self.trv_senhas.column('#2', width=50)
        self.trv_senhas.column('#3', width=100)
        self.trv_senhas.column('#4', width=100)
        self.trv_senhas.column('#5', width=100)
        self.trv_senhas.column('#6', width=100)

        self.trv_senhas.place(relx=0.00, rely=0.00, relwidth=0.96, relheight=0.99)

        self.scroll_list_senhas = ttk.Scrollbar(self.fra_bottom_senha, orient='vertical')

        self.trv_senhas.config(yscroll=self.scroll_list_senhas.set)

        self.scroll_list_senhas.place(relx=0.96, rely=0.00,
                               relwidth=0.04, relheight=0.97)

        # Lista de Usuario
        self.trv_usuarios = ttk.Treeview(self.fra_bottom_usuario, height=3, column=(
            'col1', 'col2', 'col3', 'col4', 'col5'))
        self.trv_usuarios.heading('#0', text='')
        self.trv_usuarios.heading('#1', text='Cod.')
        self.trv_usuarios.heading('#2', text='CPF')
        self.trv_usuarios.heading('#3', text='Nome')
        self.trv_usuarios.heading('#4', text='Login')
        self.trv_usuarios.heading('#5', text='Senha')

        self.trv_usuarios.column('#0', width=1)
        self.trv_usuarios.column('#1', width=49)
        self.trv_usuarios.column('#2', width=100)
        self.trv_usuarios.column('#3', width=150)
        self.trv_usuarios.column('#4', width=100)
        self.trv_usuarios.column('#5', width=100)

        self.trv_usuarios.place(relx=0.00, rely=0.00, relwidth=0.96, relheight=0.99)

        self.scroll_list_usuarios = ttk.Scrollbar(self.fra_bottom_usuario, orient='vertical')

        self.trv_usuarios.config(yscroll=self.scroll_list_usuarios.set)

        self.scroll_list_usuarios.place(relx=0.96, rely=0.00,
                                      relwidth=0.04, relheight=0.97)