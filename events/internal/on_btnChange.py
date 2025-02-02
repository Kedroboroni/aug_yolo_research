
from PySide6.QtWidgets import QFileDialog


def openDirectory(parent):
    # Открываем диалог выбора папки
    options = QFileDialog.Options()
    directory = QFileDialog.getExistingDirectory(parent, "Выберите папку", "", options=options)
    if directory:
        
        parent.setText(directory)