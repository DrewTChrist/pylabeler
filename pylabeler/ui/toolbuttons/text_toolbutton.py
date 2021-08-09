from pylabeler.ui.toolbuttons.toolbutton import ToolButton


class TextToolButton(ToolButton):

    def __init__(self):
        super().__init__()
        self.html = '<div class="draggable"><p></p></div>'
