from PySide6.QtWidgets import QSlider, QHBoxLayout, QLabel, QWidget
from PySide6.QtCore import Qt







class slider(QWidget):


    def __init__(self, min_value, max_value, step, name_param):
        super().__init__()
        self.name_param = name_param


        if min_value == 0 and max_value <= 0.01:
            self.min_value = 0
            self.max_value = 100000*max_value
            self.step = 1
            self.flag_float = True
            self.flag_1000 = True

        elif min_value == 0 and max_value <= 1:
            self.min_value = 0
            self.max_value = 100*max_value
            self.step = 1
            self.flag_float = True
            self.flag_1000 = False

        else:
            self.min_value = min_value
            self.max_value = max_value
            self.step = step
            self.flag_float = False
            self.flag_1000 = False
        
        layout = QHBoxLayout()

        self.label_name = QLabel(self.name_param)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.min_value)
        self.slider.setMaximum(self.max_value) 
        self.slider.setSingleStep(self.step)   
        self.slider.setValue(self.min_value)    

        self.label = QLabel(f"Текущее значение: {self.slider.value()}")
        self.label.setFixedWidth(180)

        self.slider.valueChanged.connect(self.updateLabel)

        layout.addWidget(self.label_name)
        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def updateLabel(self, value):
        if self.flag_float and self.flag_1000:
            self.label.setText(f"Текущее значение: {float(self.slider.value()/100000)}")
            return (self.name_param, float(self.slider.value()/100000))
    
        elif self.flag_float:
            self.label.setText(f"Текущее значение: {float(self.slider.value()/100)}")
            return (self.name_param, float(self.slider.value()/100))
        
        else:
            self.label.setText(f"Текущее значение: {self.slider.value()}")
            return (self.name_param, float(self.slider.value()))

    def currentWidget(self):
        if self.flag_float and self.flag_1000:
            return (self.name_param, float(self.slider.value()/100000))
    
        elif self.flag_float:
            return (self.name_param, float(self.slider.value()/100))
        
        else:
            return (self.name_param, float(self.slider.value()))
    
