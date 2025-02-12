from PySide6.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Tic-Tac-Toe")