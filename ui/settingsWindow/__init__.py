import time
import sys, os
sys.path.append(os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.abspath(
                    __file__
                )
            )
        )
    )
)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import QDialog, QPushButton, QScrollBar, QComboBox, QVBoxLayout, QScrollArea, QLabel, QLineEdit
from PySide6.QtCore import QSize, Qt

#Тут в класе мы должны получать с какой функцией работаем, какие настройки должно вывести окно..
class settingsWindow(QDialog):
    size = QSize(500, 170)
    
    def __init__(self, name_fun):
        super().__init__()
        self.setWindowTitle(name_fun)
        
        # Создаем элементы интерфейса
        self.layout = QVBoxLayout()
        self.label = QLabel("Введите параметры:")
        self.input_field = QLineEdit()
        self.ok_button = QPushButton("OK")
        
        # Добавляем элементы в макет
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.ok_button)
        
        self.setLayout(self.layout)

        # Подключаем сигнал кнопки
        self.ok_button.clicked.connect(self.accept)