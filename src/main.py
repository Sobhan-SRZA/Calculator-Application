import sys
from PyQt6 import QtGui
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication
from PyQt6.QtCore import QTimer, Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("calibri", 40, -1, False))
        layout.addWidget(self.label)
        self.newLabel = QLabel()
        self.newLabel.setText("© Sobhan-SRZA")
        self.newLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.newLabel.setFont(QFont("arial", 20, -1, False))
        layout.addWidget(self.newLabel)
        self.setWindowTitle("Calculator Application")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.setGeometry(100, 100, 800, 400)
        self.setLayout(layout)
        
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()