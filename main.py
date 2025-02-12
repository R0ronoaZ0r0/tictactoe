from PySide6.QtWidgets import QApplication
from src.models.main_window import MainWindow

def main():
    app = QApplication()
    window = MainWindow(app)
    window.show()
    app.exec()



if __name__ == "__main__":
    main()