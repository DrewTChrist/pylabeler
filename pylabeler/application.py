from PyQt5 import QtWidgets
from pylabeler.main import Ui_MainWindow
import sys


class Application:
    def __init__(self):
        self.qapp = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()
        sys.exit(self.qapp.exec_())
