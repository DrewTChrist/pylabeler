from PyQt5.QtWebEngineWidgets import QWebEngineView
import os


class DroppableWebEngine(QWebEngineView):

    def __init__(self, parent):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.loadFinished.connect(self.run_js)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/html'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        self.model.insert_item(e.mimeData().html())
        self.update()

    def run_js(self):
        interact = ""
        draggable = ""
        resizable = ""
        with open(os.path.normcase(os.path.join('/'.join(__file__.split('/')[0:-2]), 'assets/interact.min.js')), 'r') as file:
            interact = file.read()
            file.close()

        with open(os.path.normcase(os.path.join('/'.join(__file__.split('/')[0:-2]), 'assets/draggable.js')), 'r') as file:
            draggable = file.read()
            file.close()

        with open(os.path.normcase(os.path.join('/'.join(__file__.split('/')[0:-2]), 'assets/resizable.js')), 'r') as file:
            resizable = file.read()
            file.close()

        self.page().runJavaScript(interact)
        self.page().runJavaScript(draggable)
        self.page().runJavaScript(resizable)

    def update(self, model):
        self.page().setHtml(model.html)
