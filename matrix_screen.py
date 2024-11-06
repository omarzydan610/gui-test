from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout,QLabel

from methods_screen import Methods, MatrixScreen


class Matrix(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel("Selected Method: None", self)
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

    def display_method(self, method):
        self.label.setText(f"Selected Method: {method}")