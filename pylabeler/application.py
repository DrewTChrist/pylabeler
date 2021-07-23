from PyQt5 import QtWidgets
import qtawesome
from pylabeler.main import Ui_MainWindow
from pylabeler import icons
import sys


class Application:
    def __init__(self):
        self.qapp = QtWidgets.QApplication(sys.argv)
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.set_icons()
        self.main_window.show()
        sys.exit(self.qapp.exec_())

    def set_icons(self):
        self.main_window.setWindowIcon(qtawesome.icon(icons.barcode))
        self.ui.toolButton_qrcode.setIcon(qtawesome.icon(icons.qrcode))
        self.ui.toolButton_barcode.setIcon(qtawesome.icon(icons.barcode))
        self.ui.toolButton_image.setIcon(qtawesome.icon(icons.image))
        self.ui.toolButton_text.setIcon(qtawesome.icon(icons.text))
        self.ui.toolButton_table.setIcon(qtawesome.icon(icons.table))

