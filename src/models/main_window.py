from PySide6.QtWidgets import QMainWindow
from src.models.menu_bar import MenuBar
from src.models.game_layout import GameLayout

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Tic-Tac-Toe")

        # Menu bar
        menu_bar = MenuBar(self.app)
        self.setMenuBar(menu_bar)

        # Game layout
        game_layout = GameLayout()
        self.setCentralWidget(game_layout)
