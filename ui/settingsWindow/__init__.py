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
from PySide6.QtWidgets import QDialog, QPushButton, QWidget, QComboBox, QVBoxLayout, QMessageBox, QLineEdit, QHBoxLayout
from PySide6.QtCore import QSize, Signal
from dictsParams.manageParams import manageParams
from slider import slider





class settingsWindow(QDialog):
    size = QSize(500, 170)
    right_button_clicked = Signal(str, list)

    def __init__(self, name_fun):
        super().__init__()
        self.name_fun = name_fun
        self.setWindowTitle(f"Настройки {name_fun}")
        self.layout = QVBoxLayout()

        self.value_widgets = []
        tuple_params = manageParams(name_fun).get_params()

        for obj in tuple_params:
            if len(obj) > 2:
                comboBox = QComboBox()
                for item in obj:
                    comboBox.addItem(f"{item}")
                self.value_widgets.append(comboBox)
                self.layout.addWidget(comboBox)

            elif type(obj[0]) == bool:
                lineEdit_bool = QLineEdit("bool")
                self.value_widgets.append(lineEdit_bool)
                self.layout.addWidget(lineEdit_bool)

            elif len(obj) == 2 and obj[1] in ["int", "float"]:
                if obj[1] == "int":
                    lineEdit_min = QLineEdit(f"int min -> {obj[0][0]}")
                    lineEdit_max = QLineEdit(f"int max -> {obj[0][1]}")

                elif obj[1] == "float":
                    lineEdit_min = QLineEdit(f"float min -> {obj[0][0]}")
                    lineEdit_max = QLineEdit(f"float max -> {obj[0][1]}")

                widget_lineEdit = QWidget()
                layoutLine = QHBoxLayout()
                layoutLine.addWidget(lineEdit_min)
                layoutLine.addWidget(lineEdit_max)
                widget_lineEdit.setLayout(layoutLine)
                self.layout.addWidget(widget_lineEdit)
                tuple_value = (lineEdit_min, lineEdit_max)
                self.value_widgets.append(tuple_value)

            elif len(obj) == 2:
                step = obj[1] / 100
                slider_widget = slider(obj[0], obj[1], step)
                self.value_widgets.append(slider_widget)
                self.layout.addWidget(slider_widget)

    

        self.ok_button = QPushButton("OK")
        self.layout.addWidget(self.ok_button)
        self.setLayout(self.layout)

        self.ok_button.clicked.connect(self.accept)


    def getValues(self):
        values = {}
        for widget in self.value_widgets:
            if isinstance(widget, QComboBox):
                try:
                    values[widget] = float(widget.currentText())
                except ValueError:
                    values[widget] = str(widget.currentText())

            elif isinstance(widget, slider):
                try:
                    values[widget] = float(widget.getCurrentValue())
                except ValueError:
                    values[widget] = str(widget.currentText())

            elif isinstance(widget, tuple):
                values[widget] = (widget[0].text()), float(widget[1].text())
                #values[widget[1]] = int(widget[1].text())

            elif isinstance(widget, QLineEdit):
                if widget.text() == "False":
                    values[widget] = False
                if widget.text() == "True":
                    values[widget] = True

        return values


    def accept(self):
        try:
            self.valuesParams = tuple(self.getValues().values())
        except ValueError:
            messageError = QMessageBox(text = "Укажит верный формат!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()
            return
        
        super().accept()
        self.right_button_clicked.emit(self.name_fun, self.valuesParams)







