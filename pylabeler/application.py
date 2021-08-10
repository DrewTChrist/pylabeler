from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
from pylabeler.ui.main_window import MainWindow
import sys


class Application:

    def __init__(self):
        self._app = QApplication(sys.argv)
        apply_stylesheet(self._app, 'dark_teal.xml')
        self._main_window = MainWindow()
        self._main_window.show()
        sys.exit(self._app.exec_())
