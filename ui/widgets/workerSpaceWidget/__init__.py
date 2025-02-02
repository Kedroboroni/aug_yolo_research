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
    QDialog)
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPixmap, QImage
from widgets.sidebarWidget import sidebarWidget
from tabWidget import tabWidget
from dialogWindow import dialogWindow
from labels.sidebarLabel import sidebarLabel
from functools import partial
import time
from dialogWindow import dialogWindow
from events.internal.on_btnStart import *

def fun1():
    print("Выполнилась функция 1")

def fun2():
    print("Выполнилась функция 2")

def fun3():
    print("Выполнилась функция 3")

def fun4():
    print("Выполнилась функция 4")


class workSpaceWidget(QStackedWidget):
    
    dictParams = {
        "Название функции1": partial(fun1),
        "Название функции2": partial(fun2),
        "Название функции3": partial(fun3),
        "Название функции4": partial(fun4) }

    def __init__(self):
        
        super().__init__()
        self.placment()

        #1. В placment определить сначала приветсвенный экран!
        #2. Опеределить методы по вкладкам (1 метод - 1 вкладка и размещение там, + retunr widget)
    
    def placment(self):
         
        self.addWidget(self.welcome()) #0
        self.addWidget(self.internal()) #1
        self.addWidget(self.analyse()) #2
        self.addWidget(self.DB()) #3
        self.addWidget(self.users()) #4
        self.addWidget(self.report())


    def welcome(self):
        #!!!!сейча сбуду использовать классическую табилцу,
        #!!!!Далее нужно будет ее переопредилть, явно укзаать откуда брать данные
        #!!!!Класс таблица будет в папке tabel
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
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        self.status_ChecBox = {}

        for key, item in self.dictParams.items():
            checkBox = QCheckBox(text = key)
            self.status_ChecBox[key] = checkBox
            layout.addWidget(checkBox)

        self.btnStart = QPushButton("Push me!")
        layout.addWidget(self.btnStart)

        self.btnStart.clicked.connect(self.on_btnStart)

        self.process_running = False

        return widget
    
    def on_btnStart(self, text):

        select_box = {
            key: item
            for key, item in self.status_ChecBox.items()
            if self.status_ChecBox[key].isChecked()
        }
        text = f"Your selected CheckBox:\n {
            '\n'.join(select_box.keys())
        }"
        
        self.msg = dialogWindow(text)        
        self.msg.show()

        if not self.process_running:
            self.process_running = True
            self.msg.progressBar.setValue(0)
            self.btnStart.setEnabled(False)
            self.thread = ProcessThread()
            self.thread.finished.connect(self.msg.update_progress_bar)
            self.thread.finished.connect(self.btnStart.setEnabled)
            self.thread.finished.connect(lambda: setattr(self, 'process_running', False))
            self.thread.done.connect(self.msg.close)
            self.thread.start()

    def analyse(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        image = QImage(r"ui\widgets\workerSpaceWidget\Label3.jpg")

        self.label = QLabel()
        self.label.setScaledContents(True)
        layout.addWidget(self.label)
        self.label.setPixmap(QPixmap(image))

        return widget
        
    
    def DB(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        image = QImage(r"ui\widgets\workerSpaceWidget\Label2.jpg")

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setScaledContents(True)
        layout.addWidget(self.label)
        self.label.setPixmap(QPixmap(image))

        return widget


    def users(self):
         
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)
        layout.setAlignment(Qt.AlignCenter)

        #Создать условие для входа пользователя if asda= das 

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
    

    def report(self):

        widget = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        widget.setLayout(layout)

        image = QImage(r"ui\widgets\workerSpaceWidget\Label4.jpg")

        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setScaledContents(True)
        layout.addWidget(self.label)
        self.label.setPixmap(QPixmap(image))

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

    #l2 = QHBoxLayout()
   #secondWidget.setLayout(l2)
    
    #btn2 = QPushButton("Кнопка")
    #l2.addWidget(btn2)

    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())
        
        
        