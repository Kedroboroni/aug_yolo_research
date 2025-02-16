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
from dictsParams.manageParams import manageParams
import dictsParams

#Тут в класе мы должны получать с какой функцией работаем, какие настройки должно вывести окно..
class settingsWindow(QDialog):
    size = QSize(500, 170)

            #Размещаем компоненты настроек по имении функции
            #Для разнх-ых параметров (типов данных у них, размещаем разные widgets)

            
    def __init__(self, name_fun):
        !!!!! Добавть кнопку отмена, сделать собитие по нажатию отмена, опситаь событие по нажатию ок(применения настроек)
        super().__init__()
        self.setWindowTitle(f"Настройки {name_fun}")
        
        self.layout = QVBoxLayout()

        self.label = QLabel("Пока в разработке")
        tuple_params = manageParams(name_fun).get_params()
        for obj in tuple_params:
            !!!! добавить условия по добавлению различных типов джанных, если выбор из мин макс, то скролл бар, если из ограниченного набора, то выпад список,
            !!!! если диапазона то два ввода.
            После нажатичя на ок параметры сохраняются!!! в этом окне под новым классов manageParams, чтобы дальше передать их в partial

            if len(obj) >2:
            
                self.comboBox = QComboBox()
                for item in obj:
                    self.comboBox.addItem(f"{item}")
                #self.comboBox.addItems(obj)
                self.layout.addWidget(self.comboBox)

            else:
                self.widget = QPushButton(f"{obj}")
                self.layout.addWidget(self.widget)

        self.ok_button = QPushButton("OK")
        
        # Добавляем элементы в макет
        self.layout.addWidget(self.label)
        #self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.ok_button)
        
        self.setLayout(self.layout)

        # Подключаем сигнал кнопки
        self.ok_button.clicked.connect(self.accept)