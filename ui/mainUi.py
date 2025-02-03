from PySide6.QtWidgets import QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QApplication
from widgets import errorWidget,  sidebarWidget, workerSpaceWidget
import sys


class mainWindow(QMainWindow):

    def __init__(self):

        super().__init__()
        self.placment()
        self.app = QApplication.instance()
        self.clickedOnSidebarButton()


    def placment(self):

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)    

        layoutH = QHBoxLayout()
        layoutH.setContentsMargins(0, 0, 0, 0)
        layoutH.setSpacing(0)
        centralWidget.setLayout(layoutH)

        self.sidebarWidget = sidebarWidget.sidebarWidget()
        layoutH.addWidget(self.sidebarWidget)

        layoutV = QVBoxLayout()
        layoutV.setContentsMargins(0, 0, 0, 0)
        layoutV.setSpacing(0)
        layoutH.addLayout(layoutV)
        
        self.workerSpaceWidget = workerSpaceWidget.workSpaceWidget()
        layoutV.addWidget(self.workerSpaceWidget)

        self.errorWidget = errorWidget.errorWidget()
        layoutV.addWidget(self.errorWidget)


    def clickedOnSidebarButton(self):
         
        self.sidebarWidget.label.btnTabel.clicked.connect(lambda: self.workerSpaceWidget.setCurrentIndex(1))
        self.sidebarWidget.label.btnAnalys.clicked.connect(lambda: self.workerSpaceWidget.setCurrentIndex(2))
        self.sidebarWidget.label.btnUser.clicked.connect(lambda:  self.workerSpaceWidget.setCurrentIndex(3))




if __name__ == "__main__":

    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
            style = file.read()
            #print(style)
            app.setStyleSheet(style)
    window = mainWindow()
    window.setMinimumSize(800, 700)
    window.show()
    sys.exit(app.exec())
    