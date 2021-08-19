from pylabeler.ui.file_io_dialog import FileIoDialog
from pylabeler.ui.item_options_dialog import ItemOptionsDialog
from pylabeler.ui.main import Ui_MainWindow
from pylabeler.ui.html_tree_item import HtmlTreeItem
from pylabeler.ui.html_editor import HtmlEditor
from pylabeler.ui.about_dialog import AboutDialog
from pylabeler.ui.droppable_webengine import DroppableWebEngine
from pylabeler.ui import icons
from pylabeler import constants
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl, QSize
import qtawesome


def set_enabled_widgets(enabled, widgets):
    for widget in widgets:
        widget.setEnabled(enabled)


def open_url(url):
    QDesktopServices.openUrl(QUrl(url))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._custom_ui_setup()
        editor = HtmlEditor(self.htmlEditor)
        self.gridLayout_5.addWidget(editor, 2, 0, 1, 1)
        self.htmlTextBox = editor
        webengine = DroppableWebEngine(self.labelView)
        webengine.setMaximumSize(QSize(400, 600))
        self.gridLayout_4.addWidget(webengine, 0, 0, 1, 1)
        self.webEngineView = webengine
        self.about = AboutDialog()

    def _custom_ui_setup(self):
        self.disable_project_ui()
        self._set_icons()
        self._setup_signals()

    def _set_icons(self):
        self.toolButton_qrcode.setIcon(
            qtawesome.icon(icons.qrcode, color="white", color_active="white")
        )
        self.toolButton_barcode.setIcon(
            qtawesome.icon(icons.barcode, color="white", color_active="white")
        )
        self.toolButton_image.setIcon(
            qtawesome.icon(icons.image, color="white", color_active="white")
        )
        self.toolButton_text.setIcon(
            qtawesome.icon(icons.text, color="white", color_active="white")
        )
        self.toolButton_table.setIcon(
            qtawesome.icon(icons.table, color="white", color_active="white")
        )

    def _setup_signals(self):
        self._toolbuttons_signals()
        self.elementTree.itemClicked.connect(
            lambda: self.open_item_options_dialog(
                self.elementTree.currentItem())
        )
        self.actionAbout.triggered.connect(self.open_about)
        self.actionGet_Help.triggered.connect(
            lambda: open_url(constants.help_url)
        )

    def _toolbuttons_signals(self):
        self.toolButton_qrcode.clicked.connect(
            lambda: self.add_tree_item(HtmlTreeItem("QR Code"))
        )
        self.toolButton_barcode.clicked.connect(
            lambda: self.add_tree_item(HtmlTreeItem("Barcode"))
        )
        self.toolButton_image.clicked.connect(
            lambda: self.add_tree_item(HtmlTreeItem("Image"))
        )
        self.toolButton_text.clicked.connect(
            lambda: self.add_tree_item(HtmlTreeItem("Text"))
        )
        self.toolButton_table.clicked.connect(
            lambda: self.add_tree_item(HtmlTreeItem("Table"))
        )

    def html_model_event(self, model):
        self._update_webengineviews(model)
        self._update_text_editor(model)

    def text_editor_event(self, model):
        model.set_html(self.htmlTextBox.text())
        self.html_model_event(model)

    def _update_webengineviews(self, model):
        self.webEngineView.update(model)
        self.webEngineView_2.setHtml(model.data())

    def _update_text_editor(self, model):
        self.htmlTextBox.setText(model.data())

    def _project_ui_set_enabled(self, enabled):
        self.tabWidget.setEnabled(enabled)
        self.actionUndo.setEnabled(enabled)
        self.actionRedo.setEnabled(enabled)
        self.actionSave_Project.setEnabled(enabled)
        self.actionSave_As.setEnabled(enabled)
        self.actionClose_Project.setEnabled(enabled)

    def enable_project_ui(self):
        self._project_ui_set_enabled(True)

    def disable_project_ui(self):
        self._project_ui_set_enabled(False)

    def ui_element_set_enabled(self, attr_name, enabled):
        element_object = getattr(self, attr_name)
        element_object.setEnabled(enabled)

    def enable_ui_element(self, element):
        self.ui_element_set_enabled(element, True)

    def disable_ui_element(self, element):
        self.ui_element_set_enabled(element, False)

    def add_tree_item(self, tree_item):
        self.elementTree.addTopLevelItem(tree_item)

    def open_item_options_dialog(self, item):
        dialog = ItemOptionsDialog(item.text(0))
        dialog.dialog()
        set_enabled_widgets(False, [self.toolButtonBar, self.elementTree])
        dialog.rejected.connect(
            lambda: set_enabled_widgets(
                True, [self.toolButtonBar, self.elementTree])
        )
        dialog.accepted.connect(
            lambda: set_enabled_widgets(
                True, [self.toolButtonBar, self.elementTree])
        )

    @staticmethod
    def file_io_dialog(command):
        return FileIoDialog(command).dialog()

    def open_about(self):
        self.about.dialog()
