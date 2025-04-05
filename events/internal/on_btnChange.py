
from PySide6.QtWidgets import QFileDialog


def openDirectory(parent):
    options = QFileDialog.Options()
    directory = QFileDialog.getExistingDirectory(parent, "Выберите папку", "", options=options)
    if directory:
        
        parent.setText(directory)