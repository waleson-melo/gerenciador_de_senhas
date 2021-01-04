import tkinter as tk
import tkinter.messagebox as mb


class TemplateWindow:
    def __init__(self, root, name="Janela", size="675x550", menu=False, resx=False, resy=False):
        self.root = root
        self.root.title(name)
        self.root.geometry(size)
        self.root.resizable(resx, resy)
        self.root.minsize(550, 500)

        self.fra_root = tk.Frame(self.root)
        # self.fra_root['bg'] = 'blue'
        self.fra_root.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        if menu:
            self.menuBar()

    def window(self, root, name="JanelaSecundaria", size="675x550", resx=False, resy=False, closeAll=False):
        self.root2 = tk.Toplevel()
        self.root2.title(name)
        self.root2.geometry(size)
        self.root2.resizable(resx, resy)
        self.root2.minsize(75, 75)
        self.root2.transient(root)
        self.root2.focus_force()
        self.root2.grab_set()

        self.fra_root2 = tk.Frame(self.root2)
        self.fra_root2.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

        if closeAll:
            self.root2.protocol("WM_DELETE_WINDOW", self.quit)

    # Menu da Janela
    def menuBar(self):
        men_bar = tk.Menu(self.root)
        self.root.config(menu=men_bar)

        self.file_menu = tk.Menu(men_bar)
        self.file_menu2 = tk.Menu(men_bar)

        men_bar.add_cascade(label='Opções', menu=self.file_menu)
        men_bar.add_cascade(label='Sobre', menu=self.file_menu2)

        self.file_menu.add_command(label='Sair', command=self.quit)

    # Função de fechar a Janela
    def quit(self):
        self.root.destroy()

    def quitSecundaria(self):
        self.root2.destroy()

    # Função de Popup
    def popup(self, tip=1, tit="Titulo", msg="Menssagem"):
        if tip == 1:
            # Info
            mb.showinfo(title=tit, message=msg)
        elif tip == 2:
            # Warning
            mb.showwarning(title=tit, message=msg)
        elif tip == 3:
            # Error
            mb.showerror(title=tit, message=msg)
        elif tip == 4:
            # Ask Yes, No
            return mb.askyesno(title=tit, message=msg)


