from PySide6.QtWidgets import QLabel, QStatusBar, QHBoxLayout, QLineEdit


class errorLabel(QLabel):

    def __init__(self):

        super().__init__()


    def placment(self):

        layout = QHBoxLayout()
        self.setLayout(layout)
        
        self.informLabel = QLineEdit(text = "informe about Errors")
        layout.addWidget(self.informLabel)

        self.progressBar = QStatusBar()
        layout.addWidget(self.progressBar)
