from pylabeler.ui.toolbuttons.toolbutton import ToolButton


class ImageToolButton(ToolButton):

    def __init__(self):
        super().__init__()
        self.html = '<div class="draggable"><img src=""></div>'
