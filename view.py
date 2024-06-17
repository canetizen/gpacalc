from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtWidgets import QMainWindow

class View:
    def __init__(self):
        loader1 = QUiLoader()
        loader2 = QUiLoader()
        loader3 = QUiLoader()

        # Load main window
        ui_file1 = QFile("ui/form_main.ui")
        ui_file1.open(QFile.ReadOnly)
        self.main_window = loader1.load(ui_file1)
        ui_file1.close()

        # Load login window
        ui_file2 = QFile("ui/form_login.ui")
        ui_file2.open(QFile.ReadOnly)
        self.login_window = loader2.load(ui_file2)
        ui_file2.close()

        # Load error window
        ui_file3 = QFile("ui/form_error.ui")
        ui_file3.open(QFile.ReadOnly)
        self.error_window = loader3.load(ui_file3)
        ui_file3.close()

        # Set fixed size to prevent resizing
        for window in [self.main_window, self.login_window, self.error_window]:
            window.setFixedSize(window.size())
