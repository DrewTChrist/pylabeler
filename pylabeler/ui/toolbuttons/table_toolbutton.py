from pylabeler.ui.toolbuttons.toolbutton import ToolButton


class TableToolButton(ToolButton):

    def __init__(self):
        super().__init__()
        self.html = '<div class="draggable"><table></table></div>'
