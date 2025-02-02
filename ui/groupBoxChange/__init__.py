from PySide6.QtWidgets import QGroupBox, QVBoxLayout,  QLineEdit, QPushButton



class groupBoxChange(QGroupBox):


    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.lineEdit = QLineEdit()
        self.btnChange = QPushButton("Выбрать")

        layout.addWidget(self.lineEdit)
        layout.addWidget(self.btnChange)

        



        