import sys
from PyQt6 import (QtGui)
from PyQt6.QtGui import (QFont, QIcon)
from PyQt6.QtWidgets import (QLabel, QVBoxLayout, QApplication, QGridLayout, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QWidget)
from PyQt6.QtCore import (QTimer, Qt)
from functools import (partial)

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon('favicon.png'))
        self.setLayout(self.main_layout)
        central_widget = QWidget(self)
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)
        self.create_output()
        self.create_numpad()
        self.show()
        self.label = QLabel()
        self.label.setText("© Sobhan-SRZA")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("arial", 10, -1, False))
        self.main_layout.addWidget(self.label)

    def create_output(self):
        panel = QHBoxLayout()
        self.display = QLineEdit("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        panel.addWidget(self.display)
        backspace = QPushButton("⌫")
        backspace.clicked.connect(self.on_backspace)
        panel.addWidget(backspace)
        self.main_layout.addLayout(panel)

    def create_numpad(self):
        buttons = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            [".", "00", "0"],
            ["+", "-", "//"],
            ["*", "/", "^"],
            ["%", "Clear", "="],
        ]

        numpad = QGridLayout()

        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                btn = QPushButton(button)
                btn.clicked.connect(partial(self.on_click, button))
                numpad.addWidget(btn, i, j)

        self.main_layout.addLayout(numpad)

    def on_backspace(self):
        edit = self.get_display()[:-1]
        if edit == "" or edit.startswith("ERROR: "):
            self.set_display("0")
        else:
            self.set_display(edit)

    def on_click(self, button):
        match button:
            case "=":
                item = self.get_display().replace("^", "**")
                result = 0
                try:
                    result = eval(item)
                except SyntaxError:
                    self.set_display("ERROR: Invalid input")
                except ZeroDivisionError:
                    self.set_display("ERROR: Division by zero")
                else:
                    self.set_display(str(result))
            case "00":
                if self.get_display().startswith("ERROR: "):
                    self.set_display("0")
                elif self.get_display() != "0":
                    self.set_display(self.get_display() + "00")
            case "Clear":
                self.set_display("0")
            case "%":
                self.set_display(self.get_display() + "%")
            case _:
                if self.get_display() == "0" or self.get_display().startswith("ERROR: "):
                    self.set_display(button)
                else:
                    self.set_display(self.get_display() + button)

    def get_display(self) -> str:
        return self.display.text()

    def set_display(self, text: str):
        self.display.setText(text)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("org.codeberg.Grafcube.Calculator")
    app.setStyle('Fusion')
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()