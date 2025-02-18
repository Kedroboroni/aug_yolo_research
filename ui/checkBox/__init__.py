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
from PySide6.QtCore import Qt, Signal
from ui.settingsWindow import settingsWindow




class checkBox(QCheckBox):
    settings = None
    tunnel_signal = Signal(str, list)
    def __init__(self, text):
        super().__init__(text)
        self.name_fun = text     


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.isChecked())
               
        elif event.button() == Qt.RightButton:
            self.settings = settingsWindow(self.name_fun)
            self.settings.right_button_clicked.connect(self.tunnel_signal_settings)
            self.settings.exec_()

    def tunnel_signal_settings(self, name, params):

        self.tunnel_signal.emit(name, params)

        
                 
        
        

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