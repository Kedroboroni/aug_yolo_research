import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from PySide6.QtWidgets import QTabWidget, QWidget, QComboBox, QHBoxLayout, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas
from matplotlib.figure import Figure
from tabels import tabel1


class tabWidget(QTabWidget):

    def __init__(self, count):
        # !!! Тут вместо count будем указывтаь список с виджетами (в них размещены таблицы график, кнопки)
        super().__init__()
        self.placement()

    
    def placement(self):
            
        self.addTab(self.allTime(), "Все время")
        self.addTab(self.lastYear(), "Последний год")
        self.addTab(self.lastMonth(), "Последний месяц")
        self.addTab(self.lastWeek(), "Последний неделя")
        self.addTab(self.lastThreeDays(), "Последние 3 дня")
        self.addTab(self.lastDay(), "Последний день")
        
    
    def allTime(self):
         
        centralWidget =  QWidget()
        HLayout = QHBoxLayout()
        centralWidget.setLayout(HLayout)
        HLayout.setContentsMargins(0, 0, 0, 0)

        leftWidget = QWidget()
        HLayout.addWidget(leftWidget)

        VLayout = QVBoxLayout()
        leftWidget.setLayout(VLayout)
        VLayout.setContentsMargins(0, 0, 0, 0)
        
        comboBox = QComboBox()
        comboBox.addItem("Количетсво появлений")
        comboBox.addItem("Интенсивность появлений")
        VLayout.addWidget(comboBox)

        tabel = tabel1.tabelPage1()
        VLayout.addWidget(tabel)

        return centralWidget
    

    def lastYear(self):

        centralWidget =  QWidget()
        HLayout = QHBoxLayout()
        centralWidget.setLayout(HLayout)
        HLayout.setContentsMargins(0, 0, 0, 0)

        leftWidget = QWidget()
        HLayout.addWidget(leftWidget)

        VLayout = QVBoxLayout()
        leftWidget.setLayout(VLayout)
        VLayout.setContentsMargins(0, 0, 0, 0)
        
        comboBox = QComboBox()
        VLayout.addWidget(comboBox)

        tabel = tabel1.tabelPage1()
        VLayout.addWidget(tabel)

        comboBox.addItem("Количетсво появлений")
        comboBox.addItem("Интенсивность появлений")

        return centralWidget
    

    def lastMonth(self):
         
        centralWidget =  QWidget()
        HLayout = QHBoxLayout()
        centralWidget.setLayout(HLayout)
        HLayout.setContentsMargins(0, 0, 0, 0)

        leftWidget = QWidget()
        HLayout.addWidget(leftWidget)

        VLayout = QVBoxLayout()
        leftWidget.setLayout(VLayout)
        VLayout.setContentsMargins(0, 0, 0, 0)
        
        comboBox = QComboBox()
        VLayout.addWidget(comboBox)

        tabel = tabel1.tabelPage1()
        VLayout.addWidget(tabel)

        comboBox.addItem("Количетсво появлений")
        comboBox.addItem("Интенсивность появлений")

        return centralWidget
    

    def lastWeek(self):
        
        centralWidget =  QWidget()
        HLayout = QHBoxLayout()
        centralWidget.setLayout(HLayout)
        HLayout.setContentsMargins(0, 0, 0, 0)

        leftWidget = QWidget()
        HLayout.addWidget(leftWidget)

        VLayout = QVBoxLayout()
        leftWidget.setLayout(VLayout)
        VLayout.setContentsMargins(0, 0, 0, 0)
        
        comboBox = QComboBox()
        VLayout.addWidget(comboBox)

        tabel = tabel1.tabelPage1()
        VLayout.addWidget(tabel)

        comboBox.addItem("Количетсво появлений")
        comboBox.addItem("Интенсивность появлений")

        return centralWidget
    

    def lastThreeDays(self):
        
        centralWidget =  QWidget()
        HLayout = QHBoxLayout()
        centralWidget.setLayout(HLayout)
        HLayout.setContentsMargins(0, 0, 0, 0)

        leftWidget = QWidget()
        HLayout.addWidget(leftWidget)

        VLayout = QVBoxLayout()
        leftWidget.setLayout(VLayout)
        VLayout.setContentsMargins(0, 0, 0, 0)
        
        comboBox = QComboBox()
        VLayout.addWidget(comboBox)

        tabel = tabel1.tabelPage1()
        VLayout.addWidget(tabel)

        comboBox.addItem("Количетсво появлений")
        comboBox.addItem("Интенсивность появлений")

        return centralWidget
    

    def lastDay(self):
        
        centralWidget =  QWidget()
        HLayout = QHBoxLayout()
        centralWidget.setLayout(HLayout)
        HLayout.setContentsMargins(0, 0, 0, 0)

        leftWidget = QWidget()
        HLayout.addWidget(leftWidget)

        VLayout = QVBoxLayout()
        leftWidget.setLayout(VLayout)
        VLayout.setContentsMargins(0, 0, 0, 0)
        
        comboBox = QComboBox()
        VLayout.addWidget(comboBox)

        tabel = tabel1.tabelPage1()
        VLayout.addWidget(tabel)

        comboBox.addItem("Количетсво появлений")
        comboBox.addItem("Интенсивность появлений")


        return centralWidget

    
if __name__ == '__main__':

    from PySide6.QtWidgets import QApplication, QWidget, QMainWindow, QHBoxLayout, QPushButton
    import sys
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

    widget = tabWidget(5)
    
    l.addWidget(widget)


    window.resize(512, 300)
    window.show()
    sys.exit(app.exec())

