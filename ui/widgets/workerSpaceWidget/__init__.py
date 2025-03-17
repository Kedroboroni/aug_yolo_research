import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
from time import time
from PySide6.QtWidgets import (
    QStackedWidget,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLineEdit,
    QScrollArea,
    QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QImage
from widgets.sidebarWidget import sidebarWidget
from dialogWindow import dialogWindow
from processes.process_aug import *
from processes.process_yolo_run import *
from dictsParams import *
from groupBoxChange import groupBoxChange
from events.internal.on_btnChange import *
from ui.checkBox import checkBox
from slider_p import slider_p





class workSpaceWidget(QStackedWidget):
    
    dictParamsInternal = dictInternalAug_brightness_settings 
    dictParamsInternalTransform = dictInternalAug_transform_settings 
    dictParamsExternal = dictParamsAug_Yolo
    dictParams = {}
    dictParams_transform = {}
    dictParams_external = {}

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
        self.slider_p = slider_p()

        scroll = QScrollArea()
        scroll.setMinimumSize(QSize(512, 512))
        scroll.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        self.status_ChecBox = {}

        for key, item in self.dictParamsInternal.items():
            self.checkBox = checkBox(text = key)
            self.checkBox.tunnel_signal.connect(self.updateParams_brighets)
            self.status_ChecBox[key] = self.checkBox
            scroll_layout.addWidget(self.checkBox)
            

        scroll.setWidget(scroll_widget)

        self.btnStart = QPushButton("Начать аугументацию по выбранным функциям")
        self.btnStart.clicked.connect(self.on_btnStart_brightness_settings)

        layout.addWidget(self.boxChange)
        layout.addWidget(self.slider_p)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart)     

        self.process_running = False

        return widget
    

    def transport(self):
         
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.boxChange_transform = groupBoxChange()
        self.boxChange_transform.btnChange.clicked.connect(lambda: openDirectory(self.boxChange_transform.lineEdit))

        self.slider_p_transform = slider_p()

        scroll = QScrollArea()
        scroll.setMinimumSize(QSize(512, 512))
        scroll.setWidgetResizable(True)

        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        self.status_ChecBox_transform = {}
        self.listParams_transform = []

        for key, item in self.dictParamsInternalTransform.items():
            self.checkBox_transform = checkBox(text = key)
            self.checkBox_transform.tunnel_signal.connect(self.updateParams_transform)
            self.status_ChecBox_transform[key] = self.checkBox_transform
            scroll_layout.addWidget(self.checkBox_transform)

        scroll.setWidget(scroll_widget)

        self.btnStart_transform = QPushButton("Начать аугументацию по выбранным функциям и параметрам")
        self.btnStart_transform.clicked.connect(self.on_btnStart_transform)

        layout.addWidget(self.boxChange_transform)
        layout.addWidget(self.slider_p_transform)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart_transform)     

        self.process_running_transform = False

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
        self.listParams_external = []

        for key, item in self.dictParamsExternal.items():
            self.checkBox_external = checkBox(text=key)
            self.checkBox_external.tunnel_signal.connect(self.updateParams_external)
            self.status_ChecBox_external[key] = self.checkBox_external
            scroll_layout.addWidget(self.checkBox_external)

        scroll.setWidget(scroll_widget)

        self.btnStart_external = QPushButton("Начать аугументацию по выбранным функциям и параметрам")
        self.btnStart_external.clicked.connect(self.on_btnStart_external)

        layout.addWidget(self.boxChange_external)
        layout.addWidget(scroll)
        layout.addWidget(self.btnStart_external)     

        self.process_running_external = False

        return widget


    def updateParams_brighets(self, name_fun, dictParams):
        self.dictParams[name_fun] = partial(self.dictParamsInternal[name_fun], **dictParams)


    def updateParams_transform(self, name_fun, dictParams):
        self.dictParams_transform[name_fun] = partial(self.dictParamsInternalTransform[name_fun], **dictParams)


    def updateParams_external(self, name_param, dictParam):
        self.dictParams_external[name_param] = dictParam[name_param]


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
                self.thread = ProcessThread(path,
                                            listKeys_func,
                                            self.dictParams,
                                            self.slider_p.currentWidget(),
                                            self.slider_p.isChecked_ON_OFF()
                                        )
                self.thread.progress.connect(self.msg.update_progress_bar)
                self.thread.finished.connect(self.msg.update_progress_bar)
                self.thread.finished.connect(lambda: self.btnStart.setEnabled(True))
                self.thread.finished.connect(lambda: setattr(self, 'process_running', False))
                self.thread.finished.connect(self.dictParams.clear)
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
                self.thread_transform = ProcessThread(path_external,
                                                      listKeys_func_transform,
                                                      self.dictParams_transform,
                                                      self.slider_p_transform.currentWidget(),
                                                      self.slider_p_transfotm.isChecked_ON_OFF()
                                                    )
                self.thread_transform.progress.connect(self.msg_transform.update_progress_bar)
                self.thread_transform.finished.connect(self.msg_transform.update_progress_bar)
                self.thread_transform.finished.connect(lambda: self.btnStart_transform.setEnabled(True))
                self.thread_transform.finished.connect(lambda: setattr(self, 'process_running_transform', False))
                self.thread_transform.finished.connect(self.dictParams_transform.clear)
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
        

    def on_btnStart_external(self):

        path_external = rf"{self.boxChange_external.lineEdit.text()}"

        select_box_external = {
            key: item
            for key, item in self.status_ChecBox_external.items()
            if self.status_ChecBox_external[key].isChecked()
        }

        listKeys_func_external = list(select_box_external.keys())
        if path_external and select_box_external:
            if not self.process_running_external:
                    self.process_running_external = True
                    self.btnStart_external.setDisabled(True)
                    self.thread_external = ProcessThreadExternal(path_external,
                                                                listKeys_func_external,
                                                                self.dictParams_external,
                                                            )
                    self.thread_external.finished.connect(lambda: self.btnStart_external.setEnabled(True))
                    self.thread_external.finished.connect(lambda: setattr(self, 'process_running_external', False))
                    self.thread_external.finished.connect(self.dictParams_external.clear)
                    self.thread_external.start()

        elif select_box_external:
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
        
        
        
