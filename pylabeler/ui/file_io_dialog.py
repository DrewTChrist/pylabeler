from PyQt5.QtWidgets import QWidget, QFileDialog
from pathlib import Path


class FileIoDialog(QWidget):

    def __init__(self, command=None):
        super().__init__()
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 400
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.home = str(Path.home())
        self.command = {
            'open': self.open_project_dialog,
            'save': self.save_project_dialog,
        }[command]

    def dialog(self):
        return self.command()

    def open_project_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        return QFileDialog.getExistingDirectory(self, "Open Project", self.home, options=options)

    def save_project_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        return QFileDialog.getSaveFileName(self, "Save Project", self.home, options=options)

