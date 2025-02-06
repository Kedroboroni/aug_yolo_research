import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from PySide6.QtWidgets import (
    QStackedWidget,
    QCheckBox,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLineEdit,
    QSizePolicy,
    QScrollArea,
    QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from widgets.sidebarWidget import sidebarWidget
from dialogWindow import dialogWindow
from processes.process_aug import *
from dictsParams import *
from groupBoxChange import groupBoxChange
from events.internal.on_btnChange import *
from ui.checkBox import checkBox



#34


class workSpaceWidget(QStackedWidget):
    
    dictParamsInternal = dictInternalAug_brightness_settings # Тут должен быть список названий вощмодных функций аугументации
    dictParamsInternalTransform = dictInternalAug_transform_settings # А сейчас тут словарь.

    def __init__(self):
        
        super().__init__()
        self.placment()

    
    def placment(self):
         
        self.addWidget(self.welcome()) #0
        self.addWidget(self.internal()) #1
        self.addWidget(self.transport())
        self.addWidget(self.external()) #2
        self.addWidget(self.users()) #3



    def welcome(self):
        
        widget = QWidget()
        layout = QHBoxLayout()
        widget.setLayout(layout)
        self.setLayout(layout)
        layout.setContentsMargins(0, 0, 0, 0)

        self.welcomeLabel = QLabel()
        image = QImage(r"ui\widgets\workerSpaceWidget\welcome.jpg")
        self.welcomeLabel.setPixmap(QPixmap(image))
        self.welcomeLabel.setScaledContents(True)
        layout.addWidget(self.welcomeLabel)
        
        return widget


    def internal(self):

        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.boxChange = groupBoxChange()
        self.boxChange.btnChange.clicked.connect(lambda: openDirectory(self.boxChange.lineEdit))

        scroll = QScrollArea()
        scroll.setMinimumSize(QSize(512, 512))
        scroll.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        self.status_ChecBox = {}

        for key, item in self.dictParamsInternal.items(): # убрать item, переописать под список, все равно тут словарь не нужен
            self.checkBox = checkBox(text = key)
            self.status_ChecBox[key] = self.checkBox
            scroll_layout.addWidget(self.checkBox)
            

        scroll.setWidget(scroll_widget)

        self.btnStart = QPushButton("Начать аугументацию по выбранным функциям")
        self.btnStart.clicked.connect(self.on_btnStart_brightness_settings)

        layout.addWidget(self.boxChange)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart)     

        self.process_running = False

        return widget
    

    def transport(self):
         
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.boxChange_transform = groupBoxChange()
        self.boxChange_transform.btnChange.clicked.connect(lambda: openDirectory(self.boxChange_transform.lineEdit))

        scroll = QScrollArea()
        scroll.setMinimumSize(QSize(512, 512))
        scroll.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        self.status_ChecBox_transform = {}
        self.listParams_transform = []

        for key, item in self.dictParamsInternalTransform.items():
            self.checkBox = checkBox(text=key)
            self.status_ChecBox_transform[key] = self.checkBox
            scroll_layout.addWidget(self.checkBox)

        scroll.setWidget(scroll_widget)

        self.btnStart_transform = QPushButton("Начать аугументацию по выбранным функциям и параметрам")
        self.btnStart_transform.clicked.connect(self.on_btnStart_transform)

        layout.addWidget(self.boxChange_transform)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart_transform)     

        self.process_running_transform = False

        return widget
    

    def external(self):

        widget = QWidget()
        layout = QVBoxLayout(widget)

        return widget


    def on_btnStart_brightness_settings(self):

        path = rf"{self.boxChange.lineEdit.text()}"

        select_box = {
            key: item
            for key, item in self.status_ChecBox.items()
            if self.status_ChecBox[key].isChecked()
        }
        listKeys_func = list(select_box.keys())

        text = f"<b>Ваши выбранные функции:</b> <br>  {
            "<br>".join(select_box.keys())
        }"

        if path and select_box:
            self.msg = dialogWindow(text)        
            self.msg.show()
        
            if not self.process_running:
                self.process_running = True
                self.msg.progressBar.setValue(0)
                self.btnStart.setDisabled(True)
                self.thread = ProcessThread(path, listKeys_func)
                self.thread.progress.connect(self.msg.update_progress_bar)
                self.thread.finished.connect(self.msg.update_progress_bar)
                self.thread.finished.connect(lambda: self.btnStart.setEnabled(True))
                self.thread.finished.connect(lambda: setattr(self, 'process_running', False))
                self.thread.done.connect(self.msg.close)
                self.thread.start()
            
        elif select_box:
            messageError = QMessageBox(text = "Укажите путь!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()

            return
        
        elif path:
            messageError = QMessageBox(text = "Выберите функции!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()

            return

        else:
            messageError = QMessageBox(text = "Выберите путь и функции!!!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()

            return
                


    def on_btnStart_transform(self):

        path_external = rf"{self.boxChange_transform.lineEdit.text()}"

        select_box_transform = {
            key: item
            for key, item in self.status_ChecBox_transform.items()
            if self.status_ChecBox_transform[key].isChecked()
        }

        listKeys_func_transform = list(select_box_transform.keys())

        text = f"<b>Ваши выбранные функции:</b> <br>  {
            "<br>".join(select_box_transform.keys())
        }"
        
        if path_external and select_box_transform:
            self.msg_transform = dialogWindow(text)        
            self.msg_transform.show()

            if not self.process_running_transform:
                self.process_running_tranmsform = True
                self.msg_transform.progressBar.setValue(0)
                self.btnStart_transform.setDisabled(True)
                self.thread_transform = ProcessThread(path_external, listKeys_func_transform)
                self.thread_transform.progress.connect(self.msg_transform.update_progress_bar)
                self.thread_transform.finished.connect(self.msg_transform.update_progress_bar)
                self.thread_transform.finished.connect(lambda: self.btnStart_transform.setEnabled(True))
                self.thread_transform.finished.connect(lambda: setattr(self, 'process_running', False))
                self.thread_transform.done.connect(self.msg_transform.close)
                self.thread_transform.start()

        elif select_box_transform:
            messageError = QMessageBox(text = "Укажите путь!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()

            return
        
        elif path_external:
            messageError = QMessageBox(text = "Выберите функции!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()

            return
        
        else:
            messageError = QMessageBox(text = "Выберите путь и функции!!!")
            messageError.setWindowTitle("Ошибка")
            messageError.setIcon(QMessageBox.Warning)
            messageError.setStandardButtons(QMessageBox.Ok)
            messageError.exec_()

            return


    def users(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)

        LOGIN = QLineEdit()
        LOGIN.setFixedSize(250,50)
        layout.addWidget(LOGIN)

        PASSWORD = QLineEdit()
        PASSWORD.setFixedSize(250,50)
        PASSWORD.setEchoMode(QLineEdit.Password)
        layout.addWidget(PASSWORD)

        btnSignUP = QPushButton("Войти")
        btnSignUP.setFixedSize(250,50)
        layout.addWidget(btnSignUP)

        return widget
    




if __name__ == '__main__':

    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton
    app = QApplication(sys.argv)
    
    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  

    window = QMainWindow()
    
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    l = QHBoxLayout()

    l.setContentsMargins(0, 0, 0, 0)  
    l.setSpacing(0)
    centralWidget.setLayout(l)

    widget = sidebarWidget()
    secondWidget = workSpaceWidget()
    
    l.addWidget(widget)
    l.addWidget(secondWidget)

    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())
        
        
        