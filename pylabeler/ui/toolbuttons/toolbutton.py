from abc import ABC
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QToolButton


class ToolButton(ABC, QToolButton):

    def __init__(self, parent):
        super(ToolButton, self).__init__(parent)
        self.mimedata = None
        self.html = ''

    def mouseMoveEvent(self, event):
        self.mimedata = QMimeData()
        self.mimedata.setHtml(self.html)
        if event.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            drag.setMimeData(self.mimedata)
            drag.exec_(Qt.MoveAction)
