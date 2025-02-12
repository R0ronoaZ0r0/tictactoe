from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from src.models.scores_widget import ScoresWidget

class GameLayout(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rock, Paper, Scissors")

        # create layout
        layout = QVBoxLayout()

        label = QLabel("Choose your weapon:")
        label.setAlignment(Qt.AlignCenter)
        
        
        # inner layout for buttons
        child_layout = QHBoxLayout()

        # Create the buttons
        rock = QPushButton("Rock")
        paper = QPushButton("Paper")
        scissors = QPushButton("Scissors")

        # Add the buttons to the layout
        child_layout.addWidget(rock)
        child_layout.addWidget(paper)
        child_layout.addWidget(scissors)

        
        # add label and inner layout to main layout
        layout.addWidget(label)
        layout.addLayout(child_layout)

        # create and add scores widget to main layout
        scores_widget = ScoresWidget()
        layout.addWidget(scores_widget, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)