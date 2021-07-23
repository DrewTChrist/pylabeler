from PyQt5.QtWidgets import QWidget, QFileDialog


class FileIoDialog(QWidget):

    def __init__(self, command=None):
        super().__init__()
        self.title = 'Open Project'
        self.setWindowTitle(self.title)
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 400
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.command = {
            'open': self.open_project_dialog,
            'save': self.save_project_dialog,
            'saveas': self.save_project_dialog_as,
        }[command]

    def dialog(self):
        value = self.command()
        self.show()
        return value

    def open_project_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.ShowDirsOnly
        filename = QFileDialog.getExistingDirectory(self, "Open Project", ".", options=options)
        return filename

    def save_project_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)

    def save_project_as_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)
