import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) #~\ui
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy
from PySide6.QtWidgets import QLabel, QVBoxLayout
from PySide6.QtCore import Qt
from buttons.sidebarButtons import userButton, tabelButton, dbButton, analysButton, reportButton
#from widgets.workerSpaceWidget import workSpaceWidget



class sidebarLabel(QLabel):

    def __init__(self):

        super().__init__()
        self.placment()


    def placment(self):

        layout = QVBoxLayout()
        self.setLayout(layout)
        
        self.btnTabel = tabelButton.tabelButton()
        self.btnAnalys = analysButton.analysButton()
        self.btnReport = reportButton.reportButton()
        self.btnDB = dbButton.dbButton()
        self.btnUser = userButton.userButton()
        self.spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(self.btnTabel)
        layout.addWidget(self.btnAnalys)
        layout.addWidget(self.btnReport)
        layout.addItem(self.spacer)
        layout.addWidget(self.btnDB)
        layout.addWidget(self.btnUser)
        layout.setAlignment(Qt.AlignCenter)

    


      




if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton
    app = QApplication(sys.argv)
    with open(f"{os.path.dirname(
                os.path.dirname(
                os.path.dirname(
                os.path.abspath(__file__))))}\SpyBot.qss", "r") as file:
            style = file.read()
            app.setStyleSheet(style)  
    window = QMainWindow()
    centralWidget = QWidget()
    window.setCentralWidget(centralWidget)
    l = QHBoxLayout()
    centralWidget.setLayout(l)

    label = sidebarLabel()
    secondWidget = QWidget()

    l.addWidget(label)
    l.addWidget(secondWidget)


    l2 = QHBoxLayout()
    secondWidget.setLayout(l2)
    
    btn2 = QPushButton("Кнопка")
    l2.addWidget(btn2)

    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())