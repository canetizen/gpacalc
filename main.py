from controller import Controller
from PySide6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

controller = Controller()
sys.exit(app.exec_())