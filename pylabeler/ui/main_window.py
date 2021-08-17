from pylabeler.ui.file_io_dialog import FileIoDialog
from pylabeler.ui.item_options_dialog import ItemOptionsDialog
from pylabeler.ui.main import Ui_MainWindow
from pylabeler.ui.html_tree_item import HtmlTreeItem
from pylabeler.ui.html_editor import HtmlEditor
from pylabeler.ui.about_dialog import AboutDialog
from pylabeler.ui.droppable_webengine import DroppableWebEngine
from pylabeler.ui import icons
from pylabeler.html_model import HtmlModel
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QColor, QDesktopServices
from PyQt5.QtCore import QUrl, QSize
import qtawesome
import os


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
        self.model = HtmlModel()
        self.model.dataChanged.connect(self._html_model_event)
        self.htmlTextBox.textChanged.connect(self._text_editor_event)
        webengine = DroppableWebEngine(self.labelView)
        webengine.setMaximumSize(QSize(400, 600))
        self.gridLayout_4.addWidget(webengine, 0, 0, 1, 1)
        self.webEngineView = webengine
        self.about = None

        self.current_project = {
            "project_name": None,
            "project_directory": None,
            "data_source": None,
            "html": None,
            "saved": False,
        }

    def _custom_ui_setup(self):
        self._disable_project_ui()
        self._set_icons()
        self._setup_signals()

    def _set_icons(self):
        self.setWindowIcon(qtawesome.icon(icons.barcode))
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
        self._menubar_signals()
        self.elementTree.itemClicked.connect(
            lambda: self.open_item_options_dialog(
                self.elementTree.currentItem())
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

    def _html_model_event(self):
        self._update_webengineviews()
        self._update_text_editor()

    def _text_editor_event(self):
        self.model.set_html(self.htmlTextBox.text())
        self._html_model_event()

    def _update_webengineviews(self):
        self.webEngineView.update(self.model)
        self.webEngineView_2.setHtml(self.model.data())

    def _update_text_editor(self):
        self.htmlTextBox.setText(self.model.data())

    def _menubar_signals(self):
        self.actionNew_Project.triggered.connect(self.new_project)
        self.actionOpen_Project.triggered.connect(self.open_project)
        self.actionClose_Project.triggered.connect(self.close_project)
        self.actionSave_Project.triggered.connect(self.save_project)
        self.actionSave_As.triggered.connect(self.save_project_as)
        self.actionAbout.triggered.connect(self.open_about)
        self.actionGet_Help.triggered.connect(
            lambda: open_url("https://drewtchrist.github.io/pylabeler")
        )

    def _project_ui_set_enabled(self, enabled):
        self.tabWidget.setEnabled(enabled)
        self.actionUndo.setEnabled(enabled)
        self.actionRedo.setEnabled(enabled)
        self.actionSave_Project.setEnabled(enabled)
        self.actionSave_As.setEnabled(enabled)
        self.actionClose_Project.setEnabled(enabled)

    def _enable_project_ui(self):
        self._project_ui_set_enabled(True)

    def _disable_project_ui(self):
        self._project_ui_set_enabled(False)

    def _write_html_to_file(self):
        label_path = os.path.join(
            str(self.current_project["project_directory"]), "label.html")
        with open(label_path, "w") as file:
            file.write(self.model.html)
        file.close()

    def add_tree_item(self, tree_item):
        self.elementTree.addTopLevelItem(tree_item)

    def new_project(self):
        self.model.load_base()
        self.current_project = {
            "project_name": None,
            "project_directory": None,
            "data_source": None,
            "html": self.model.html,
            "saved": False,
        }
        self._enable_project_ui()

    def open_project(self):
        io_dialog = FileIoDialog("open")
        self.current_project["project_directory"] = io_dialog.dialog()
        io_dialog.close()
        label_path = os.path.join(
            str(self.current_project["project_directory"]), "label.html"
        )
        if os.path.exists(self.current_project["project_directory"]) and os.path.exists(
                label_path
        ):
            try:
                with open(label_path, "r") as file:
                    self.model.set_html(file.read())
                    file.close()
            except Exception as e:
                print(e)

            self.current_project["saved"] = True
            self._enable_project_ui()
            self.actionSave_Project.setEnabled(False)

    def close_project(self):
        self.current_project = {
            "project_name": None,
            "project_directory": None,
            "data_source": None,
            "html": None,
            "saved": False,
        }
        self.model.set_html("")
        self._disable_project_ui()

    def save_project(self):
        if not self.current_project["saved"]:
            self.save_project_as()
        else:
            self._write_html_to_file()
            self.actionSave_Project.setEnabled(False)

    def save_project_as(self):
        io_dialog = FileIoDialog("save")
        directory = io_dialog.dialog()[0]
        if directory:
            self.current_project["project_directory"] = directory
            self.current_project["project_name"] = self.current_project["project_directory"].split(
                "/")[-1]
            os.mkdir(os.path.join(self.current_project["project_directory"]))
            self._write_html_to_file()
            self.current_project["saved"] = True
            self.actionSave_Project.setEnabled(False)

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

    def open_about(self):
        self.about = AboutDialog()
        self.about.dialog()
