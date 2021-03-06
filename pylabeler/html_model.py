from PyQt5.QtCore import QAbstractItemModel, QModelIndex
import os


class HtmlModel(QAbstractItemModel):

    def __init__(self):
        super(HtmlModel, self).__init__()
        self.html = ""

    def data(self):
        return self.html

    def load_base(self):
        with open(os.path.join(os.path.split(__file__)[0], 'assets', 'base.html'), 'r') as file:
            self.html = file.read()
            file.close()
        self.dataChanged.emit(QModelIndex(), QModelIndex())

    def set_html(self, html):
        self.html = html
        self.dataChanged.emit(QModelIndex(), QModelIndex())
