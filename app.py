from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from pylabeler.main import Ui_MainWindow


class PyLabeler(QtWidgets.QMainWindow):
    def __init__(self):
        super(PyLabeler, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = PyLabeler()
    form.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
