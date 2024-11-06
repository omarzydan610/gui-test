import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QPushButton
from methods_screen import Methods
from matrix_screen import Matrix


from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

from methods_screen import Methods, MatrixScreen


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stacked Widget Example")
        self.setGeometry(100, 100, 800, 600)

        # Create QStackedWidget to manage multiple pages
        self.stacked_widget = QStackedWidget(self)

        # Create two pages
        self.methods_page = Methods(self.stacked_widget)
        self.matrix_screen_page = MatrixScreen()

        # Add pages to QStackedWidget
        self.stacked_widget.addWidget(self.methods_page)
        self.stacked_widget.addWidget(self.matrix_screen_page)

        # Set the layout of the main window
        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
