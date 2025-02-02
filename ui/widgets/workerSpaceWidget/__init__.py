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
    QScrollArea)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from widgets.sidebarWidget import sidebarWidget
from dialogWindow import dialogWindow
from processes.process_aug import *
from dictsParams import *
from groupBoxChange import groupBoxChange
from events.internal.on_btnChange import *






class workSpaceWidget(QStackedWidget):
    
    dictParamsInternal = dictInternalAug_brightness_settings
    dictParamsExternal = dictInternalAug_transform_settings #Переделать под yolo

    def __init__(self):
        
        super().__init__()
        self.placment()

    
    def placment(self):
         
        self.addWidget(self.welcome()) #0
        self.addWidget(self.internal()) #1
        self.addWidget(self.external()) #2
        self.addWidget(self.DB()) #3
        self.addWidget(self.users()) #4
        self.addWidget(self.report())


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

        for key, item in self.dictParamsInternal.items():
            checkBox = QCheckBox(text=key)
            self.status_ChecBox[key] = checkBox
            scroll_layout.addWidget(checkBox)

        scroll.setWidget(scroll_widget)

        self.btnStart = QPushButton("Начать аугументацию по выбранным функциям")
        self.btnStart.clicked.connect(self.on_btnStart_brightness_settings)

        layout.addWidget(self.boxChange)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart)     

        self.process_running = False

        return widget
    

    def external(self):
         
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.boxChange_external = groupBoxChange()
        self.boxChange_external.btnChange.clicked.connect(lambda: openDirectory(self.boxChange_external.lineEdit))

        scroll = QScrollArea()
        scroll.setMinimumSize(QSize(512, 512))
        scroll.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        self.status_ChecBox_external = {}

        for key, item in self.dictParamsExternal.items():
            checkBox = QCheckBox(text=key)
            self.status_ChecBox_external[key] = checkBox
            scroll_layout.addWidget(checkBox)

        scroll.setWidget(scroll_widget)

        self.btnStart_external = QPushButton("Начать аугументацию по выбранным функциям и параметрам")
        self.btnStart_external.clicked.connect(self.on_btnStart_trasform)

        layout.addWidget(self.boxChange_external)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart_external)     

        self.process_running_external = False

        return widget
    

    def on_btnStart_brightness_settings(self):

        path = rf"{self.boxChange.lineEdit.text()}"
        if path:
            pass

        else:
            pass

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
            self.btnStart.setDisabled(True)
            self.thread = ProcessThread(path)!!!!!!!!!!!! То же самое с path продлеать в transform Так же добавить функции и сделать аугументациююююю!!!!
            self.thread.progress.connect(self.msg.update_progress_bar)
            self.thread.finished.connect(self.msg.update_progress_bar)
            self.thread.finished.connect(lambda: self.btnStart.setEnabled(True))
            self.thread.finished.connect(lambda: setattr(self, 'process_running', False))
            self.thread.done.connect(self.msg.close)
            self.thread.start()

    def on_btnStart_trasform(self):

        select_box = {
            key: item
            for key, item in self.status_ChecBox_external.items()
            if self.status_ChecBox_external[key].isChecked()
        }
        text = f"Your selected CheckBox:\n {
            '\n'.join(select_box.keys())
        }"
        
        self.msg_external = dialogWindow(text)        
        self.msg_external.show()

        if not self.process_running_external:
            self.process_running_external = True
            self.msg_external.progressBar.setValue(0)
            self.btnStart_external.setDisabled(True)
            self.thread_external = ProcessThread()
            self.thread_external.progress.connect(self.msg_external.update_progress_bar)
            self.thread_external.finished.connect(self.msg_external.update_progress_bar)
            self.thread_external.finished.connect(lambda: self.btnStart_external.setEnabled(True))
            self.thread_external.finished.connect(lambda: setattr(self, 'process_running', False))
            self.thread_external.done.connect(self.msg_external.close)
            self.thread_external.start()
        
    
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
        
        
        