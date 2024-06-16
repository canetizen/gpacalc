from controller import Controller
from PySide6 import QtCore, QtWidgets
import sys


QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts) # to prevent an error??

app = QtWidgets.QApplication(sys.argv)

controller = Controller()

sys.exit(app.exec())