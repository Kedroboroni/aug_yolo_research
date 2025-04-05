from PySide6.QtWidgets import QLineEdit, QHBoxLayout, QLabel, QWidget, QMessageBox
from PySide6.QtCore import Qt







class lineEdit(QWidget):


    def __init__(self, name_param, values):
        super().__init__()
        self.name_param = name_param

        layout = QHBoxLayout(self)

        if values[1] == "int":
            label_min_param = QLabel(f"{name_param}: min int ->")
            label_max_param = QLabel("max int ->")
            self.lineEdit_min = QLineEdit(f"{values[0][0]}")
            self.lineEdit_max = QLineEdit(f"{values[0][1]}")

        elif values[1] == "float":
            label_min_param = QLabel(f"{name_param}: min float ->")
            label_max_param = QLabel("max float ->")
            self.lineEdit_min = QLineEdit(f"{values[0][0]}")
            self.lineEdit_max = QLineEdit(f"{values[0][1]}")

        layout.addWidget(label_min_param)
        layout.addWidget(self.lineEdit_min)
        layout.addWidget(label_max_param)
        layout.addWidget(self.lineEdit_max)
        self.setLayout(layout)

    def currentWidget(self):

        try:
            return (self.name_param, (float(self.lineEdit_min.text()), float(self.lineEdit_max.text())))
        
        except ValueError:
            messageError = QMessageBox(text = "Укажите правильный формат данных")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()



if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
    import sys

    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  
    window = QWidget()
    layout = QVBoxLayout()
    btn1 = lineEdit("1123123", [(8, 10), 'int'])
    window.setLayout(layout)
    layout.addWidget(btn1)
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())





        
    

