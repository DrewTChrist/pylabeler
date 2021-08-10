from PyQt5.QtWidgets import QDialog 
from pylabeler.ui.about import Ui_aboutDialog


class AboutDialog(QDialog):

    def __init__(self, command=None):
        super().__init__()
        self.title = 'About'
        self.setWindowTitle(self.title)
        self.ui = Ui_aboutDialog()
        self.setFixedSize(350, 175)

    def dialog(self):
        self.ui.setupUi(self)
        self.show()

