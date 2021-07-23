from PyQt5 import QtWidgets
import qtawesome
from pylabeler.main import Ui_MainWindow
from pylabeler.html_tree_item import HtmlTreeItem
from pylabeler import icons
import sys


class Application:

    def __init__(self):
        self.__qapp = QtWidgets.QApplication(sys.argv)
        self.__main_window = QtWidgets.QMainWindow()
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(self.__main_window)
        self.__custom_ui_setup()
        self.__main_window.show()

        self.current_project = {

        }

        sys.exit(self.__qapp.exec_())

    def __custom_ui_setup(self):
        self.__set_icons()
        self.__setup_signals()

    def __set_icons(self):
        self.__main_window.setWindowIcon(qtawesome.icon(icons.barcode))
        self.__ui.toolButton_qrcode.setIcon(qtawesome.icon(icons.qrcode))
        self.__ui.toolButton_barcode.setIcon(qtawesome.icon(icons.barcode))
        self.__ui.toolButton_image.setIcon(qtawesome.icon(icons.image))
        self.__ui.toolButton_text.setIcon(qtawesome.icon(icons.text))
        self.__ui.toolButton_table.setIcon(qtawesome.icon(icons.table))

    def __setup_signals(self):
        self.__toolbuttons_signals()

    def __toolbuttons_signals(self):
        self.__ui.toolButton_qrcode.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('QR Code')))
        self.__ui.toolButton_barcode.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Barcode')))
        self.__ui.toolButton_image.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Image')))
        self.__ui.toolButton_text.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Text')))
        self.__ui.toolButton_table.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Table')))

    def add_tree_item(self, tree_item):
        self.__ui.elementTree.addTopLevelItem(tree_item)
