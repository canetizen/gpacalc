import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

class View:
    def __init__(self):
        loader = QUiLoader()

        ui_file = QFile("ui/form_main.ui")
        ui_file.open(QFile.ReadOnly)
        self.main_window = loader.load(ui_file)
        ui_file.close()

        ui_file = QFile("ui/form_login.ui")
        ui_file.open(QFile.ReadOnly)
        self.login_window = loader.load(ui_file)
        ui_file.close()

        ui_file = QFile("ui/form_error.ui")
        ui_file.open(QFile.ReadOnly)
        self.error_window = loader.load(ui_file)
        ui_file.close()