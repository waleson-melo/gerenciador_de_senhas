import tkinter as tk


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

    def menuBar(self):
        men_bar = tk.Menu(self.root)
        self.root.config(menu=men_bar)

        self.file_menu = tk.Menu(men_bar)
        self.file_menu2 = tk.Menu(men_bar)

        men_bar.add_cascade(label='Opções', menu=self.file_menu)
        men_bar.add_cascade(label='Sobre', menu=self.file_menu2)

        self.file_menu.add_command(label='Sair', command=self.quit)

    def quit(self):
        self.root.destroy()
