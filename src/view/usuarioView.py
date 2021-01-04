import tkinter as tk
import tkinter.ttk as ttk

import src.view.templateWindow as tw
import src.controller.usuarioController as uc


class UsuarioView(tw.TemplateWindow):
    def __init__(
            self, fra_top_senha, fra_top_usuario,
            fra_bottom_senha, fra_bottom_usuario
    ):

        self.fra_top_senha = fra_top_senha
        self.fra_top_usuario = fra_top_usuario
        self.fra_bottom_senha = fra_bottom_senha
        self.fra_bottom_usuario = fra_bottom_usuario

        self.usuario_controller = uc.UsuarioController()

    # Labels da Janela
    def labelsUsuario(self):
        # Aba 2 Usuario
        self.lbl_cpf_usuario = tk.Label(self.fra_top_usuario, text='CPF:')
        self.lbl_nome_usuario = tk.Label(self.fra_top_usuario, text='Nome:')
        self.lbl_telefone_usuario = tk.Label(self.fra_top_usuario, text='Telefone:')
        self.lbl_senha_usuario = tk.Label(self.fra_top_usuario, text='Senha:')

        self.lbl_cpf_usuario.place(relx=0.05, rely=0.05)
        self.lbl_nome_usuario.place(relx=0.41, rely=0.05)
        self.lbl_telefone_usuario.place(relx=0.05, rely=0.32)
        self.lbl_senha_usuario.place(relx=0.41, rely=0.32)

    # Entrys da Janela
    def entrysUsuario(self):
        # Aba 2 Usuario
        self.ent_codigo_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_cpf_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_nome_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_telefone_usuario = tk.Entry(self.fra_top_usuario)
        self.ent_senha_usuario = tk.Entry(self.fra_top_usuario)

        self.ent_cpf_usuario.place(relx=0.05, rely=0.16, relwidth=0.34, relheight=0.14)
        self.ent_nome_usuario.place(relx=0.41, rely=0.16, relwidth=0.34, relheight=0.14)
        self.ent_telefone_usuario.place(relx=0.05, rely=0.43, relwidth=0.34, relheight=0.14)
        self.ent_senha_usuario.place(relx=0.41, rely=0.43, relwidth=0.34, relheight=0.14)

    # Buttons da Janela
    def buttonsUsuario(self):
        # Aba 2 Usuario
        self.btn_salvar_usuario = tk.Button(self.fra_top_usuario, text='Salvar', bd=3)
        self.btn_limpar_usuario = tk.Button(self.fra_top_usuario, text='Limpar', bd=3)
        self.btn_pesquisar_usuario = tk.Button(self.fra_top_usuario, text='Pesquisar', bd=3)
        self.btn_apagar_usuario = tk.Button(self.fra_top_usuario, text='Apagar', bd=3)

        self.btn_salvar_usuario.place(relx=0.78, rely=0.16, relwidth=0.18, relheight=0.21)
        self.btn_limpar_usuario.place(relx=0.78, rely=0.37, relwidth=0.18, relheight=0.21)
        self.btn_pesquisar_usuario.place(relx=0.78, rely=0.58, relwidth=0.18, relheight=0.21)
        self.btn_apagar_usuario.place(relx=0.78, rely=0.79, relwidth=0.18, relheight=0.21)

        self.btn_salvar_usuario['command'] = self.saveUsuario
        self.btn_limpar_usuario['command'] = self.clearEntryUsuario
        self.btn_pesquisar_usuario['command'] = self.searchUsuario
        self.btn_apagar_usuario['command'] = self.deleteUsuario

    # Lista da Janela
    def listUsuario(self):
        # Lista de Usuario
        self.trv_usuarios = ttk.Treeview(self.fra_bottom_usuario, height=3, column=(
            'col1', 'col2', 'col3', 'col4', 'col5'))
        self.trv_usuarios.heading('#0', text='')
        self.trv_usuarios.heading('#1', text='Cod.')
        self.trv_usuarios.heading('#2', text='CPF')
        self.trv_usuarios.heading('#3', text='Nome')
        self.trv_usuarios.heading('#4', text='Telefone')
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

        # Logica do Duplo Click
        self.trv_usuarios.bind('<Double-1>', self.onDoubleClickUsuario)

    # Limpar as estradas do Usuario
    def clearEntryUsuario(self):
        self.ent_codigo_usuario.delete(0, tk.END)
        self.ent_cpf_usuario.delete(0, tk.END)
        self.ent_nome_usuario.delete(0, tk.END)
        self.ent_telefone_usuario.delete(0, tk.END)
        self.ent_senha_usuario.delete(0, tk.END)

    # Limpar a lista do usuario
    def clearListUsuarios(self):
        self.trv_usuarios.delete(*self.trv_usuarios.get_children())

    # Pegar os dados das entradas do Usuario
    def getEntryUsuario(self):
        self.codigo_usuario = str(self.ent_codigo_usuario.get()).strip()
        self.cpf_usuario = str(self.ent_cpf_usuario.get()).strip()
        self.nome_usuario = str(self.ent_nome_usuario.get()).strip().lower()
        self.telefone_usuario = str(self.ent_telefone_usuario.get()).strip()
        self.senha_usuario = str(self.ent_senha_usuario.get()).strip()

        cond = [
            self.cpf_usuario != '',
            self.nome_usuario != '',
            self.telefone_usuario != '',
            self.senha_usuario != '',
        ]

        if all(cond):
            return True
        else:
            return False

    # Função de duplo click na lista de usuario
    def onDoubleClickUsuario(self, event):
        self.clearEntryUsuario()
        self.trv_usuarios.selection()

        for i in self.trv_usuarios.selection():
            col1, col2, col3, col4, col5 = self.trv_usuarios.item(i, 'values')

            self.ent_codigo_usuario.insert(tk.END, col1)
            self.ent_cpf_usuario.insert(tk.END, col2)
            self.ent_nome_usuario.insert(tk.END, col3)
            self.ent_telefone_usuario.insert(tk.END, col4)
            self.ent_senha_usuario.insert(tk.END, col5)

    # Lista todos os dados de usuario na list
    def addUsuariolist(self):
        self.clearEntryUsuario()
        self.clearListUsuarios()
        dados = self.usuario_controller.searchAllUsuarios()
        for dado in dados:
            self.trv_usuarios.insert("", tk.END, values=dado)

    #-----------------------------------------------------------------------------

    # Funçoes do Usuario
    def saveUsuario(self):
        x = self.getEntryUsuario()

        if x:
            # Verificado se o campo codigo esta vazio, se estiver o usuario é salvo como novo, senao e alterado
            if self.codigo_usuario == '':
                # Chamar função do controller pra salvar no Banco
                ret = self.usuario_controller.saveUsuario(
                    self.cpf_usuario, self.nome_usuario, self.telefone_usuario, self.senha_usuario
                )

                # Se o cadastro for bem sucedido mostrar ok, senao erro
                if ret[0]:
                    self.clearEntryUsuario()
                    self.addUsuariolist()
                    self.popup(tip=1, tit='ATENÇÂO', msg='Usuário salvo com sucesso.')
                else:
                    self.popup(tip=3, tit='ERRO', msg='Erro ao salvar usuário. ' + ret[1])
            else:
                # Chamar função do controller pra alterar no Banco
                ret = self.usuario_controller.updateUsuario(
                    self.codigo_usuario, self.cpf_usuario, self.nome_usuario, self.telefone_usuario,
                    self.senha_usuario
                )

                # Se a alteração for bem sucedida mostrar ok, senao erro
                if ret[0]:
                    self.clearEntryUsuario()
                    self.addUsuariolist()
                    self.popup(tip=1, tit='ATENÇÂO', msg='Usuário alterado com sucesso.')
                else:
                    self.popup(tip=3, tit='ERRO', msg='Erro ao alterar usuário. ' + ret[1])
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Preencha os campos obrigatórios.')

    # Passa os dados das Entrys para o controller pesquisar no banco
    def searchUsuario(self):
        self.getEntryUsuario()

        if self.cpf_usuario != '':
            # Chamar função do controller pra pesquisar no Banco
            ret = self.usuario_controller.searchUsuario(self.cpf_usuario)

            # Se o dado for encontrado ok, senao erro
            if ret is not None:
                # Inserindo os dados encontrados nos Entrys
                self.clearEntryUsuario()
                self.ent_codigo_usuario.insert(tk.END, (ret[0][0]))
                self.ent_cpf_usuario.insert(tk.END, ret[0][1])
                self.ent_nome_usuario.insert(tk.END, (ret[0][2]).capitalize())
                self.ent_telefone_usuario.insert(tk.END, ret[0][3])
                self.ent_senha_usuario.insert(tk.END, ret[0][4])
            else:
                self.popup(tip=2, tit='ATENÇÂO', msg='Usuário não encontrado.')
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Preencha o campo CPF para pesquisar usuário.')

    # Passa os dados das Entrys para o controller deletar do banco
    def deleteUsuario(self):
        self.getEntryUsuario()

        if self.codigo_usuario != '':
            yesno = self.popup(tip=4, tit='ATENÇÂO', msg='Deseja apagar este usuário?')
            if yesno:
                # Chamar função do controller pra apagar no Banco
                ret = self.usuario_controller.deleteUsuario(self.codigo_usuario)

                # Se for apagado com sucesso mostrar ok, senao erro
                if ret[0]:
                    self.clearEntryUsuario()
                    self.addUsuariolist()
                    self.popup(tip=1, tit='ATENÇÂO', msg='Usuário apagado com sucesso.')
                else:
                    self.popup(tip=3, tit='ERRO', msg='Erro ao apagar usuário. ' + ret[1])
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Selecione ou pesquise um usuário.')

