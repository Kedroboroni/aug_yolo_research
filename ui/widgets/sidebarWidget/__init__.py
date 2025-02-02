import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt
from labels.sidebarLabel import sidebarLabel



class sidebarWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.setFixedWidth(78)
        self.placement()
        

    def placement(self):

        layout = QVBoxLayout()
    
        self.label = sidebarLabel()

        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        

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
    secondWidget = QWidget()
    
    l.addWidget(widget)
    l.addWidget(secondWidget)

    l2 = QHBoxLayout()
    secondWidget.setLayout(l2)
    
    btn2 = QPushButton("Кнопка")
    l2.addWidget(btn2)

    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())
