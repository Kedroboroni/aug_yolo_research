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
from PySide6.QtWidgets import (QDialog,
                               QPushButton,
                               QWidget,
                               QComboBox,
                               QVBoxLayout,
                               QHBoxLayout,
                               QMessageBox,
                               QLineEdit,
                               QHBoxLayout,
                               QLabel)
from PySide6.QtCore import QSize, Signal
from dictsParams.manageParams import manageParams
from slider import slider
from comboBox import comboBox
from lineEdit import lineEdit





class settingsWindow(QDialog):
    size = QSize(500, 170)
    right_button_clicked_successful = Signal(str, dict)

    def __init__(self, name_fun):
        super().__init__()
        self.name_fun = name_fun
        self.setWindowTitle(f"Настройки {name_fun}")
        self.layout = QVBoxLayout()

        self.value_widgets = []
        dict_params = manageParams(name_fun).get_params()

        for name_param, values in dict_params.items():
            if len(values) > 2:
                param_widget = comboBox(name_param, values)
                self.layout.addWidget(param_widget)

            elif type(values[0]) == bool:
                param_widget = comboBox(name_param, values)
                self.layout.addWidget(param_widget)

            elif len(values) == 2 and values[1] in ["int", "float"]:
                
                param_widget = lineEdit(name_param, values)
                self.layout.addWidget(param_widget)

            elif len(values) == 2:
                step = values[1] / 100
                param_widget = slider(values[0], values[1], step, name_param)
                self.layout.addWidget(param_widget)
            
            self.value_widgets.append(param_widget)

        self.ok_button = QPushButton("OK")
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(self.accept)


    def getValues(self):
        self.dictValues = {}

        for widget in self.value_widgets:
            self.dictValues[widget.currentWidget()[0]] = widget.currentWidget()[1]

        return self.dictValues


    def accept(self):
        
        super().accept()
        dictParam = self.getValues()
        self.right_button_clicked_successful.emit(self.name_fun, dictParam)







