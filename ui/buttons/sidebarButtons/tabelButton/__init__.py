import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize
from parent import sidebarButton





class tabelButton(sidebarButton):

    def __init__(self):

        super().__init__()

        icon_path = r"ui\buttons\sidebarButtons\tabelButton\tabel.png"
        icon = QIcon(QPixmap(icon_path))
        self.setIcon(icon)
        self.setIconSize(QSize(50, 50))

        

        

if __name__ == "__main__":

    from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

    app = QApplication(sys.argv)
    with open(r"ui\SpyBot.qss", "r") as file:
        style = file.read()
        app.setStyleSheet(style)  
    window = QWidget()
    layout = QVBoxLayout()
    btn1 = tabelButton()
    window.setLayout(layout)
    layout.addWidget(btn1)
    window.resize(300, 200)
    window.show()
    sys.exit(app.exec())
