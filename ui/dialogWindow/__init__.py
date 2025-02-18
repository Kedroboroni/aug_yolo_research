import sys
from PySide6.QtWidgets import QLabel, QVBoxLayout, QScrollArea, QDialog, QProgressBar
from PySide6.QtCore import QSize, Qt



class dialogWindow(QDialog):
    size = QSize(500, 170)
    
    def __init__(self, information):      

        super().__init__()
        self.setWindowTitle("Выбранные функции")
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)

        self.setFixedSize(QSize(510,210)) 

        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(5, 5, 5, 5)

        scroll = QScrollArea()
        scroll.setFixedSize(self.size)
        scroll.setWidgetResizable(True)

        label = QLabel(information)
        label.setWordWrap(True)
        label.setTextInteractionFlags(Qt.TextSelectableByMouse) 

        scroll.setWidget(label)
        
        self.progressBar = QProgressBar()
        self.progressBar.setAlignment(Qt.AlignCenter)

        mainLayout.addWidget(scroll)
        mainLayout.addWidget(self.progressBar)

    
    def update_progress_bar(self, value):
        self.progressBar.setValue(value)



if __name__ == "__main__":

    import sys
    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

    app = QApplication(sys.argv)

    msg = dialogWindow("Это очень длинный текст, который не поместится в окно без прокрутки. "
        "Он будет автоматически прокручиваться, если его размер превысит размер окна. "
        "Вы можете изменять размер окна, чтобы увидеть, как текст адаптируется.\n\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
        "Это очень длинный текст, который не поместится в окно без прокрутки.\n "
        "Он будет автоматически прокручиваться, если его размер превысит размер окна. "
        "Вы можете изменять размер окна, чтобы увидеть, как текст адаптируется.\n\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
    msg.show()
    sys.exit(app.exec())