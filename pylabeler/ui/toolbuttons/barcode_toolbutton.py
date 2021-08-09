from pylabeler.ui.toolbuttons.toolbutton import ToolButton


class BarcodeToolButton(ToolButton):

    def __init__(self):
        super().__init__()
        self.html = '<div class="draggable"><img src="{{ label_tools.qr_code(value) }}"></div>'
