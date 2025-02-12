from PySide6.QtWidgets import QMenuBar

class MenuBar(QMenuBar):
    def __init__(self, app):
        super().__init__()
        self.app = app

        file_menu = self.addMenu('&File')
        quit_action = file_menu.addAction('Quit', self.quit)


    def quit(self):
        self.app.quit()