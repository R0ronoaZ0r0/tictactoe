from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout, QGridLayout
from PySide6.QtCore import Qt

class ScoresWidget(QWidget):
    def __init__(self):
        super().__init__()
        
        self.user_score = "0"
        self.cpu_score = "0"

        # define scores label
        label = QLabel("Scores")
        label.setAlignment(Qt.AlignCenter)

        # create grid layout
        layout = QGridLayout()
        layout.setAlignment(Qt.AlignCenter)
        # add widgets to grid layout
        # Row 0
        layout.addWidget(label, 0, 0, 1, 3)

        # Row 1
        layout.addWidget(QLabel("User"), 1, 0)
        layout.addWidget(QLabel("vs"), 1, 1)
        layout.addWidget(QLabel("CPU"), 1, 2)


        # Row 2
        user_score_label = QLabel(self.user_score)
        cpu_score_label = QLabel(self.cpu_score)
        vs_score_label = QLabel(":")
        

        layout.addWidget(user_score_label, 2, 0)
        layout.addWidget(vs_score_label, 2, 1)
        layout.addWidget(cpu_score_label, 2, 2)

        # set layout
        self.setLayout(layout)

    def update_scores(self, user_score, cpu_score):
        self.user_score = user_score
        self.cpu_score = cpu_score



