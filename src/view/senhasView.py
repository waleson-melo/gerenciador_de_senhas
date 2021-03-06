import tkinter as tk
import tkinter.ttk as ttk

import src.view.templateWindow as tw
import src.controller.senhasController as sc


class SenhasView(tw.TemplateWindow):
    def __init__(
            self, fra_top_senha, fra_top_usuario,
            fra_bottom_senha, fra_bottom_usuario
    ):

        self.fra_top_senha = fra_top_senha
        self.fra_top_usuario = fra_top_usuario
        self.fra_bottom_senha = fra_bottom_senha
        self.fra_bottom_usuario = fra_bottom_usuario

        self.senhas_controller = sc.SenhasController()

    # Labels da Janela
    def labelsSenha(self):
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

    # Entrys da Janela
    def entrysSenha(self):
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

    # Buttons da Janela
    def buttonsSenha(self):
        # Aba 1 Senhas
        self.btn_salvar_senha = tk.Button(self.fra_top_senha, text='Salvar', bd=3)
        self.btn_limpar_senha = tk.Button(self.fra_top_senha, text='Limpar', bd=3)
        self.btn_pesquisar_senha = tk.Button(self.fra_top_senha, text='Pesquisar', bd=3)
        self.btn_apagar_senha = tk.Button(self.fra_top_senha, text='Apagar', bd=3)

        self.btn_salvar_senha.place(relx=0.78, rely=0.16, relwidth=0.18, relheight=0.21)
        self.btn_limpar_senha.place(relx=0.78, rely=0.37, relwidth=0.18, relheight=0.21)
        self.btn_pesquisar_senha.place(relx=0.78, rely=0.58, relwidth=0.18, relheight=0.21)
        self.btn_apagar_senha.place(relx=0.78, rely=0.79, relwidth=0.18, relheight=0.21)

        self.btn_salvar_senha['command'] = self.saveSenha
        self.btn_limpar_senha['command'] = self.clearEntrySenha
        self.btn_pesquisar_senha['command'] = self.searchSenha
        self.btn_apagar_senha['command'] = self.deleteSenha

    # Lista da Janela
    def listSenha(self):
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
        self.trv_senhas.column('#1', width=19)
        self.trv_senhas.column('#2', width=30)
        self.trv_senhas.column('#3', width=100)
        self.trv_senhas.column('#4', width=100)
        self.trv_senhas.column('#5', width=100)
        self.trv_senhas.column('#6', width=140)

        self.trv_senhas.place(relx=0.00, rely=0.00, relwidth=0.96, relheight=0.99)

        self.scroll_list_senhas = ttk.Scrollbar(self.fra_bottom_senha, orient='vertical')

        self.trv_senhas.config(yscroll=self.scroll_list_senhas.set)

        self.scroll_list_senhas.place(relx=0.96, rely=0.00,
                               relwidth=0.04, relheight=0.97)

        # Logica do Duplo Click
        self.trv_senhas.bind('<Double-1>', self.onDoubleClickSenha)

    # Limpar as entradas das Senhas
    def clearEntrySenha(self):
        self.ent_codigo_senha.delete(0, tk.END)
        self.ent_nome_senha.delete(0, tk.END)
        self.ent_login_senha.delete(0, tk.END)
        self.ent_senha_senha.delete(0, tk.END)
        self.ent_observacao_senha.delete('1.0', tk.END)

    # Limpar a lista de senhas
    def clearListSenhas(self):
        self.trv_senhas.delete(*self.trv_senhas.get_children())

    # Pegar os dados das entradas da Senha
    def getEntrySenha(self):
        self.codigo_senha = str(self.ent_codigo_senha.get()).strip()
        self.nome_senha = str(self.ent_nome_senha.get()).strip().lower()
        self.login_senha = str(self.ent_login_senha.get()).strip()
        self.senha_senha = str(self.ent_senha_senha.get()).strip()
        self.observacao_senha = str(self.ent_observacao_senha.get('1.0', tk.END)).strip().lower()
        self.tipo_senha = self.tip_var_senha.get().lower()

        condi = [
            self.nome_senha != '',
            self.login_senha != '',
            self.senha_senha != ''
        ]

        if all(condi):
            return True
        else:
            return False

    # Função de duplo click na lista de senha
    def onDoubleClickSenha(self, event):
        self.clearEntrySenha()
        self.trv_senhas.selection()

        for i in self.trv_senhas.selection():
            col1, col2, col3, col4, col5, col6 = self.trv_senhas.item(i, 'values')
            self.ent_codigo_senha.insert(tk.END, col1)
            self.tip_var_senha.set(col2.capitalize())
            self.ent_nome_senha.insert(tk.END, col3.capitalize())
            self.ent_login_senha.insert(tk.END, col4)
            self.ent_senha_senha.insert(tk.END, col5)
            self.ent_observacao_senha.insert(tk.END, col6.capitalize())

    # Lista todos os dados de senhas na list
    def addSenhaslist(self):
        self.clearEntrySenha()
        self.clearListSenhas()
        dados = self.senhas_controller.searchAllSenhas()
        for dado in dados:
            self.trv_senhas.insert("", tk.END, values=dado)

    #-----------------------------------------------------------------------------

    # Funçoes da Senha
    # Passa os dados das Entrys para o controller salvar no banco
    def saveSenha(self):
        x = self.getEntrySenha()

        if x:
            # Verificado se o campo codigo esta vazio, se estiver a senha é salva como nova, senao e alterada
            if self.codigo_senha == '':
                # Chamar função do controller pra salvar no Banco
                ret = self.senhas_controller.saveSenha(
                    self.nome_senha, self.tipo_senha, self.login_senha, self.senha_senha,
                    self.observacao_senha
                )

                # Se o cadastro for bem sucedido mostrar ok, senao erro
                if ret[0]:
                    self.clearEntrySenha()
                    self.addSenhaslist()
                    self.popup(tip=1, tit='ATENÇÂO', msg='Senha salva com sucesso.')
                else:
                    self.popup(tip=3, tit='ERRO', msg='Erro ao salvar senha. ' + ret[1])
            else:
                # Chamar função do controller pra alterar no Banco
                ret = self.senhas_controller.updateSenha(
                    self.codigo_senha, self.nome_senha, self.tipo_senha, self.login_senha,
                    self.senha_senha, self.observacao_senha
                )

                # Se a alteração for bem sucedida mostrar ok, senao erro
                if ret[0]:
                    self.clearEntrySenha()
                    self.addSenhaslist()
                    self.popup(tip=1, tit='ATENÇÂO', msg='Senha alterada com sucesso.')
                else:
                    self.popup(tip=3, tit='ERRO', msg='Erro ao alterar senha. ' + ret[1])
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Preencha os campos obrigatórios.')

    # Passa os dados das Entrys para o controller pesquisar no banco
    def searchSenha(self):
        self.getEntrySenha()

        if self.nome_senha != '':
            # Chamar função do controller pra pesquisar no Banco
            ret = self.senhas_controller.searchSenha(self.nome_senha)

            # Se o dado for encontrado ok, senao erro
            if ret is not None:
                # Inserindo os dados encontrados nos Entrys
                self.clearEntrySenha()
                self.ent_codigo_senha.insert(tk.END, (ret[0][0]))
                self.tip_var_senha.set((ret[0][1]).capitalize())
                self.ent_nome_senha.insert(tk.END, (ret[0][2]).capitalize())
                self.ent_login_senha.insert(tk.END, ret[0][3])
                self.ent_senha_senha.insert(tk.END, ret[0][4])
                self.ent_observacao_senha.insert(tk.END, (ret[0][5]).capitalize())
            else:
                self.popup(tip=2, tit='ATENÇÂO', msg='Senha não encontrada.')
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Preencha o campo Nome para pesquisar senha.')

    # Passa os dados das Entrys para o controller deletar do banco
    def deleteSenha(self):
        self.getEntrySenha()

        if self.codigo_senha != '':
            yesno = self.popup(tip=4, tit='ATENÇÂO', msg='Deseja apagar esta senha?')
            if yesno:
                # Chamar função do controller pra apagar no Banco
                ret = self.senhas_controller.deleteSenha(self.codigo_senha)

                # Se for apagado com sucesso mostrar ok, senao erro
                if ret[0]:
                    self.clearEntrySenha()
                    self.addSenhaslist()
                    self.popup(tip=1, tit='ATENÇÂO', msg='Senha apagada com sucesso.')
                else:
                    self.popup(tip=3, tit='ERRO', msg='Erro ao apagar senha. ' + ret[1])
        else:
            self.popup(tip=2, tit='ATENÇÂO', msg='Selecione ou pesquise uma senha.')
