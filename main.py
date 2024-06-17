from controller import Controller
from PySide6 import QtCore, QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)

controller = Controller()

sys.exit(app.exec())