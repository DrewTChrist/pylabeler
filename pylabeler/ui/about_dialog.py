from PyQt5.QtWidgets import QDialog
from pylabeler.ui.about import Ui_aboutDialog
from pylabeler import constants


class AboutDialog(QDialog):

    def __init__(self):
        super().__init__()
        self.title = 'About'
        self.setWindowTitle(self.title)
        self.ui = Ui_aboutDialog()
        self.setFixedSize(350, 175)
        self.ui.setupUi(self)
        self.ui.label_4.setText(f'Version: {constants.help_version}')

    def dialog(self):
        self.show()
