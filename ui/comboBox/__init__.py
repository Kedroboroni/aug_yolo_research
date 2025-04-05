from PySide6.QtWidgets import QComboBox, QHBoxLayout, QLabel, QWidget
from PySide6.QtCore import Qt




def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class comboBox(QWidget):


    def __init__(self, name_param, values):
        super().__init__()
        self.values = values
        self.name_param = name_param
       
        layout_param = QHBoxLayout()
        label_nameParam = QLabel(name_param)
        self.comboBox = QComboBox()

        for item in values:
            self.comboBox.addItem(f"{item}")
        

        layout_param.addWidget(label_nameParam)
        layout_param.addWidget(self.comboBox)
        self.setLayout(layout_param)


    def currentWidget(self):
        if self.comboBox.currentText() == "False":
            return (self.name_param, False)
        
        elif self.comboBox.currentText() == "True":
            return (self.name_param, False)
        
        elif is_float(self.comboBox.currentText()):
            return (self.name_param, float(self.comboBox.currentText()))

        else:
            return (self.name_param, str(self.comboBox.currentText()))
        

