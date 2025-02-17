from PySide6.QtWidgets import QSlider, QHBoxLayout, QLabel, QWidget
from PySide6.QtCore import Qt







class slider(QWidget):


    def __init__(self, min_value, max_value, step):

        super().__init__()

        if min_value == 0 and max_value//10 == 0:
            self.min_value = 0
            self.max_value = 100*max_value
            self.step = 1
            self.flag_float = True

        else:
            self.min_value = min_value
            self.max_value = max_value
            self.step = step
            self.flag_float = False
        
        layout = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(self.min_value)
        self.slider.setMaximum(self.max_value) 
        self.slider.setSingleStep(self.step)   
        self.slider.setValue(self.min_value)    

        self.label = QLabel(f"Текущее значение: {self.slider.value()}")
        self.label.setFixedWidth(150)

        self.slider.valueChanged.connect(self.updateLabel)

        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        self.setLayout(layout)

    def updateLabel(self, value):
        if self.flag_float:
             self.label.setText(f"Текущее значение: {value/100}")

        else:
            self.label.setText(f"Текущее значение: {value}")

    def getCurrentValue(self):
        if self.flag_float:
            return self.slider.value()/100
        
        else:
            return self.slider.value()
    

if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
    import sys

    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  
    window = QWidget()
    layout = QVBoxLayout()
    btn1 = slider(1, 100, 1)
    window.setLayout(layout)
    layout.addWidget(btn1)
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())