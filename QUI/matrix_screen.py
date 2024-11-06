from PyQt6.QtWidgets import *
from PyQt6.QtGui import QDoubleValidator
from PyQt6.QtCore import Qt

class Matrix(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setStyleSheet("""
                padding: 10px;
                margin: 0px 0px;
                font-size: 40px;
                            """)
        # Main layout for the entire widget
        self.main_layout = QVBoxLayout()

        # Top layout for the back button
        self.top_layout = QHBoxLayout()

        back_button = QPushButton("Back to Methods", self)
        back_button.clicked.connect(self.go_back_to_methods)
        back_button.setStyleSheet("""
            QPushButton {
                background-color: lightblue;
                color: white;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #ddf3fa;
            }
        """)

        self.top_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        # Label for the selected method
        self.label = QLabel(self)
        self.label.setStyleSheet("""
            QLabel {
                font-size: 18px;
                font-weight: bold;
                color: black;
                margin-left: 20px;
            }
        """)
        self.top_layout.addWidget(self.label)

        # Add top layout to main layout
        self.main_layout.addLayout(self.top_layout)
        self.input_layout = QHBoxLayout()

        # Input for number of significant figures
        self.sfigures_label = QLabel("Number of Significant Figures:", self)
        self.sfigures_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                margin-top: 20px;
            }
        """)
        self.input_layout.addWidget(self.sfigures_label)

        self.sfigures_input = QSpinBox(self)
        self.sfigures_input.setMinimum(1)  # Default is 1
        self.sfigures_input.setMaximum(15)  # You can set a limit for demonstration
        self.sfigures_input.setValue(1)  # Default value is 1
        self.sfigures_input.setStyleSheet("""
            QSpinBox {
                font-size: 16px;
                padding: 5px;
                margin-top: 10px;
            }
        """)
        self.input_layout.addWidget(self.sfigures_input)

        # Input for matrix size
        self.size_label = QLabel("Enter the size of the matrix (n x n):", self)
        self.size_label.setStyleSheet("""
            QLabel {
                font-size: 16px;
                margin-top: 20px;
            }
        """)
        self.input_layout.addWidget(self.size_label)

        self.size_input = QSpinBox(self)
        self.size_input.setMinimum(1)
        self.size_input.setMaximum(9)  # For demonstration, limit to 10x10 matrix
        self.size_input.valueChanged.connect(self.generate_matrix)
        self.size_input.setStyleSheet("""
            QSpinBox {
                font-size: 16px;
                padding: 5px;
                margin-top: 10px;
            }
        """)
        self.input_layout.addWidget(self.size_input)

        # Add the horizontal layout to the main layout
        self.main_layout.addLayout(self.input_layout)

        # Create a QScrollArea for the matrix grid
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)  # Allow resizing of the content inside the scroll area
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        # Placeholder for the matrix grid
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout(self.grid_widget)
        self.grid_layout.setHorizontalSpacing(0) 
        self.scroll_area.setWidget(self.grid_widget)

        # Add the scroll area to the main layout
        self.main_layout.addWidget(self.scroll_area)

        # Solve Button
        self.solve_button = QPushButton("Solve", self)
        self.solve_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.solve_button.clicked.connect(self.solve_matrix)  # Connect to your solve function
        self.solve_button.setFixedWidth(200)

        # Center the solve button
        self.solve_layout = QHBoxLayout()
        self.solve_layout.addWidget(self.solve_button, alignment=Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addLayout(self.solve_layout)

        # Set the main layout for the widget
        self.setLayout(self.main_layout)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def display_method(self, method):
        self.label.setText(f"Selected Method: {method}")

    def go_back_to_methods(self):
        self.stacked_widget.setCurrentIndex(0)

    def generate_matrix(self):
        # Clear any existing input fields
        clear_layout(self.grid_layout)

        matrix_size = self.size_input.value()

        # Dynamically create input fields for the matrix
        self.matrix_inputs = []
        for i in range(matrix_size):
            row_inputs = []
            for j in range(matrix_size + 1):
                temp = QHBoxLayout()
                input_field = QLineEdit("0.0", self)  # Default to float format
                input_field.setStyleSheet("""
                    QLineEdit {
                        box-sizing: border-box;
                        font-size: 14px;
                        border: 1px solid #ccc;
                        padding: 5;
                        margin: 0;
                        border-radius: 5px;
                    }
                """)

                # Add the QDoubleValidator to ensure only floats are accepted
                validator = QDoubleValidator(self)
                validator.setBottom(-float('inf'))  # Allow negative floats
                validator.setTop(float('inf'))  # Allow large values
                input_field.setValidator(validator)

                temp.addWidget(input_field)

                if j == matrix_size:
                    temp2 = QLabel("")
                elif j == matrix_size - 1:
                    temp2 = QLabel(f"X{j + 1} = ")
                else:
                    temp2 = QLabel(f"X{j + 1} + ")

                temp2.setStyleSheet("margin: 0; padding: 0")
                temp2.setStyleSheet("font-size: 12px; font-weight: bold")
                temp.addWidget(temp2)
                temp.setSpacing(0)
                self.grid_layout.addLayout(temp, i, j)
                row_inputs.append(input_field)
            self.matrix_inputs.append(row_inputs)

    def solve_matrix(self):
        # Handle the solve matrix functionality here
        print("Solve button clicked!")

def clear_layout(layout: QLayout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            # If the item is a widget, delete it
            item.widget().deleteLater()
        elif item.layout():
            # If the item is a layout, recursively clear it
            clear_layout(item.layout())
