from PyQt5.QtCore import QAbstractItemModel


class HtmlModel(QAbstractItemModel):

    def __init__(self, html=None, *args, **kwargs):
        super(HtmlModel, self).__init__(*args, **kwargs)
        self.html = html or ""

    def data(self):
        return self.html
