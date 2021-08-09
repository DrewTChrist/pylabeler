from PyQt5.QtWidgets import QDialog
from pylabeler.ui import barcode_dialog
from pylabeler.ui import qrcode_dialog
from pylabeler.ui import image_dialog
from pylabeler.ui import text_dialog
from pylabeler.ui import table_dialog


class ItemOptionsDialog(QDialog):

    def __init__(self, command=None):
        super().__init__()
        self.title = 'Open Project'
        self.setWindowTitle(self.title)
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 400
        self.ui = None
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.command = {
            'barcode': self.open_barcode_options_dialog,
            'qrcode': self.open_qrcode_options_dialog,
            'image': self.open_image_options_dialog,
            'text': self.open_text_options_dialog,
            'table': self.open_table_options_dialog
        }[command.lower().replace(' ', '')]

    def dialog(self):
        value = self.command()
        self.show()
        return value

    def open_barcode_options_dialog(self):
        self.ui = barcode_dialog.Ui_barcodeDialog()
        self.ui.setupUi(self)

    def open_qrcode_options_dialog(self):
        self.ui = qrcode_dialog.Ui_qrcodeDialog()
        self.ui.setupUi(self)

    def open_image_options_dialog(self):
        self.ui = image_dialog.Ui_imageDialog()
        self.ui.setupUi(self)

    def open_text_options_dialog(self):
        self.ui = text_dialog.Ui_textDialog()
        self.ui.setupUi(self)

    def open_table_options_dialog(self):
        self.ui = table_dialog.Ui_tableDialog()
        self.ui.setupUi(self)

