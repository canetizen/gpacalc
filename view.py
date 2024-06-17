from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class View:
    def __init__(self):
        self.main_window = None
        self.error_window = None
        self.login_window = None
        self.setupView()

    def setupView(self):
        loader = QUiLoader()

        ui_file_main = QFile("ui/form_main.ui")
        ui_file_main.open(QFile.ReadOnly)
        self.main_window = loader.load(ui_file_main)
        ui_file_main.close()

        ui_file_login = QFile("ui/form_login.ui")
        ui_file_login.open(QFile.ReadOnly)
        self.login_window = loader.load(ui_file_login)
        ui_file_login.close()

        ui_file_error = QFile("ui/form_error.ui")
        ui_file_error.open(QFile.ReadOnly)
        self.error_window = loader.load(ui_file_error)
        ui_file_error.close()

        # Set fixed size to prevent resizing
        for window in [self.main_window, self.login_window, self.error_window]:
            window.setFixedSize(window.size())

    def add_row(self):
        self.main_window.table.insertRow(self.main_window.table.rowCount())
        if self.main_window.button_delete_course.isEnabled() == False:
            self.main_window.button_delete_course.setEnabled(True)
            self.main_window.button_calculate.setEnabled(True)
            self.main_window.button_clear_table.setEnabled(True)
        self.main_window.label.setText("")

    def delete_row(self):
        selected_ranges = self.main_window.table.selectedRanges()
        rows_to_delete = set()
        for selected_range in selected_ranges:
            top_row = selected_range.topRow()
            bottom_row = selected_range.bottomRow()
            rows_to_delete.update(range(top_row, bottom_row + 1))
        for row in sorted(rows_to_delete, reverse=True):
            self.main_window.table.removeRow(row)

        if self.main_window.table.rowCount() == 0:
            self.main_window.button_delete_course.setEnabled(False)
            self.main_window.button_clear_table.setEnabled(False)
            self.main_window.button_calculate.setEnabled(False)
            self.main_window.button_pull.setEnabled(True)
        self.main_window.label.setText("")

    def clear_table(self):
        self.main_window.table.setRowCount(0)
        self.main_window.button_delete_course.setEnabled(False)
        self.main_window.button_clear_table.setEnabled(False)
        self.main_window.button_pull.setEnabled(True)
        self.main_window.button_calculate.setEnabled(False)
        self.main_window.label.setText("")

    def login(self):
        self.login_window.button_login.setEnabled(True)
        self.login_window.input_password.setText("")
        self.login_window.input_username.setText("")
        self.login_window.show()

    def show_error(self, message):
        self.error_window.label.setText(f"Hata: {message}")
        self.error_window.show()