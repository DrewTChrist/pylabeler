from PyQt5.Qt import QTreeWidgetItem
from PyQt5.QtGui import QFont, QColor


class HtmlTreeItem(QTreeWidgetItem):
    def __init__(self, text='', font_size=12, set_bold=True):
        super().__init__()
        font = QFont('Open Sans', font_size)
        font.setBold(set_bold)
        self.setFont(0, font)
        self.setText(0, text)
