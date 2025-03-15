from PySide6.QtWidgets import QSlider, QHBoxLayout, QLabel, QWidget, QRadioButton
from PySide6.QtCore import Qt







class slider_p(QWidget):


    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()

        self.label_name = QLabel("Вероятность аугументации")

        self.slider_p = QSlider(Qt.Horizontal)
        self.slider_p.setMinimum(0)
        self.slider_p.setMaximum(100) 
        self.slider_p.setSingleStep(1)   
        self.slider_p.setValue(100)    

        self.label = QLabel(f"Текущее значение: {self.slider_p.value()/100}")
        self.label.setFixedWidth(210)

        self.slider_p.valueChanged.connect(self.updateLabel)

        self.rbtn_on = QRadioButton("ON")
        self.rbtn_off = QRadioButton("OFF")

        layout.addWidget(self.label_name)
        layout.addWidget(self.slider_p)
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn_on)
        layout.addWidget(self.rbtn_off)

        self.setLayout(layout)

    def updateLabel(self, value):    
        self.label.setText(f"Текущее значение: {float(self.slider_p.value()/100)}")
        return (float(self.slider_p.value()/100))


    def currentWidget(self):
        self.label.setText(f"Текущее значение: {float(self.slider_p.value()/100)}")
        return (float(self.slider_p.value()/100))
    

    def isChecked_ON_OFF(self):

        if self.rbtn_off.isChecked():
            return 2
        
        if self.rbtn_on.isChecked():
            return 1
    

if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication, QVBoxLayout
    import sys

    app = QApplication(sys.argv)

    # Создаем основной виджет
    main_window = QWidget()
    custom_checkbox = slider_p()
    #custom_checkbox2 = checkBox("Настройки2")


    # Устанавливаем основной виджет
    main_window.setLayout(QVBoxLayout())
    main_window.layout().addWidget(custom_checkbox)
    #main_window.layout().addWidget(custom_checkbox2)
    main_window.show()

    sys.exit(app.exec())


    
