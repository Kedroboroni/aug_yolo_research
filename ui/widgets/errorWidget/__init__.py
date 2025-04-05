import sys, os
sys.path.append(os.path.dirname(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from PySide6.QtWidgets import QWidget, QVBoxLayout
from labels.errorLabel import errorLabel


class errorWidget(QWidget):

    def __init__(self):

        super().__init__()
        self.setFixedHeight(90)
        self.placement()
        

    def placement(self):

        layout = QVBoxLayout()
    
        label = errorLabel()

        layout.addWidget(label)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
