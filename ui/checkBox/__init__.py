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
from PySide6.QtWidgets import QCheckBox
from PySide6.QtCore import Qt
from ui.settingsWindow import settingsWindow




class checkBox(QCheckBox):

    def __init__(self, text):
        super().__init__(text)
        self.name_fun = text
    def mousePressEvent(self, event):
        
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.isChecked())  

        elif event.button() == Qt.RightButton:
            settings = settingsWindow(f"Настройки {self.name_fun}")
            settings.exec_()
            
        
        

if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
    app = QApplication(sys.argv)

    # Создаем основной виджет
    main_window = QWidget()
    custom_checkbox = checkBox("Настройки")
    custom_checkbox2 = checkBox("Настройки2")


    # Устанавливаем основной виджет
    main_window.setLayout(QVBoxLayout())
    main_window.layout().addWidget(custom_checkbox)
    main_window.layout().addWidget(custom_checkbox2)
    main_window.show()

    sys.exit(app.exec())