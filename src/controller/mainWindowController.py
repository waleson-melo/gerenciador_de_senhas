import src.view.mainWindowView as mw


class MainWindowController:
    def __init__(self):
        self.mew = mw.MainWindowView()

    def run(self):
        self.mew.start()