from PyQt5.QtWidgets import QApplication
from pylabeler.ui.main_window import MainWindow
import sys


class Application:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self._main_window = MainWindow()
        self._main_window.show()
        sys.exit(self._app.exec_())
