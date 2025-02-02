from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QSizePolicy, QPushButton, QLineEdit
from PySide6.QtCore import Qt, QSize

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()
window.setLayout(layout)

#btn = QPushButton("Hello")
#layout.addWidget(btn)

label = QLineEdit("Мой QLabel")
label.setText("Hello")      
#label.setBaseSize(QSize(200,200))
label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
#label.setAlignment(Qt.AlignCenter)

window.show()

app.exec_()