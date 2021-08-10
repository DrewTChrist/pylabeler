from pylabeler.ui.file_io_dialog import FileIoDialog
from pylabeler.ui.item_options_dialog import ItemOptionsDialog
from pylabeler.ui.main import Ui_MainWindow
from pylabeler.ui.html_tree_item import HtmlTreeItem
from pylabeler.ui.html_editor import HtmlEditor
from pylabeler.ui import icons
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QColor
import qtawesome
import os


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self._custom_ui_setup()
        editor = HtmlEditor(self.htmlEditor)
        self.gridLayout_5.addWidget(editor, 2, 0, 1, 1)
        self.htmlTextBox = editor
        #self.htmlTextBox.SendScintilla(self.htmlTextBox.SCI_MARGINSETSTYLE, self.htmlTextBox.STYLE_DEFAULT, QColor(255, 0, 0))

        self.current_project = {
            'project_name': None,
            'project_directory': None,
            'data_source': None,
            'html': None,
            'css': None,
            'saved': False
        }

    def _custom_ui_setup(self):
        self._disable_project_ui()
        self._set_icons()
        self._setup_signals()

    def _set_icons(self):
        self.setWindowIcon(qtawesome.icon(icons.barcode))
        self.toolButton_qrcode.setIcon(qtawesome.icon(icons.qrcode))
        self.toolButton_barcode.setIcon(qtawesome.icon(icons.barcode))
        self.toolButton_image.setIcon(qtawesome.icon(icons.image))
        self.toolButton_text.setIcon(qtawesome.icon(icons.text))
        self.toolButton_table.setIcon(qtawesome.icon(icons.table))

    def _setup_signals(self):
        self._toolbuttons_signals()
        self._menubar_signals()
        self.elementTree.itemClicked.connect(lambda: self.open_item_options_dialog(self.elementTree.currentItem()))

    def _toolbuttons_signals(self):
        self.toolButton_qrcode.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('QR Code')))
        self.toolButton_barcode.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Barcode')))
        self.toolButton_image.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Image')))
        self.toolButton_text.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Text')))
        self.toolButton_table.clicked.connect(lambda: self.add_tree_item(HtmlTreeItem('Table')))

    def _update_webengineviews(self, html=None):
        if type(html) == str:
            self.webEngineView.setHtml(html)
            self.webEngineView_2.setHtml(html)
        else:
            self.webEngineView.setHtml(f"{self.current_project['html']}{self.current_project['css']}")
            self.webEngineView_2.setHtml(f"{self.current_project['html']}{self.current_project['css']}")

    def _menubar_signals(self):
        self.actionNew_Project.triggered.connect(self.new_project)
        self.actionOpen_Project.triggered.connect(self.open_project)
        self.actionClose_Project.triggered.connect(self.close_project)
        self.actionSave_Project.triggered.connect(self.save_project)
        self.actionSave_As.triggered.connect(self.save_project_as)

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
        label_path = os.path.join(self.current_project['project_directory'], 'label.html')
        with open(label_path, 'w') as file:
            file.write(f"{self.current_project['html']}<style>{self.current_project['css']}</style>")
        file.close()

    def add_tree_item(self, tree_item):
        self.elementTree.addTopLevelItem(tree_item)

    def new_project(self):
        self.current_project = {
            'project_name': None,
            'project_directory': None,
            'data_source': None,
            'html': '<h1>New Label</h1>',
            'css': '<style>h1 {text-align: center;}</style>',
            'saved': False
        }
        self._update_webengineviews()
        self._enable_project_ui()
        #self.htmlTextBox.SendScintilla(self.htmlTextBox.SCI_STYLESETBACK, self.htmlTextBox.STYLE_DEFAULT, QColor(255, 0, 0))

    def open_project(self):
        io_dialog = FileIoDialog('open')
        self.current_project['project_directory'] = io_dialog.dialog()
        io_dialog.close()
        label_path = os.path.join(self.current_project['project_directory'], 'label.html')
        if os.path.exists(self.current_project['project_directory']) and os.path.exists(label_path):
            try:
                with open(label_path, 'r') as file:
                    self.current_project['html'] = file.read()
                    self.current_project['css'] = self.current_project['html'][self.current_project['html'].find('<style>'):self.current_project['html'].find('</style>')]
                    file.close()
            except Exception as e:
                print(e)

            self.current_project['saved'] = True
            self._update_webengineviews()
            self._enable_project_ui()
            self.actionSave_Project.setEnabled(False)

    def close_project(self):
        self.current_project = {
            'project_name': None,
            'project_directory': None,
            'data_source': None,
            'html': None,
            'css': None,
            'saved': False
        }
        self._update_webengineviews('')
        self._disable_project_ui()

    def save_project(self):
        if not self.current_project['saved']:
            self.save_project_as()
            self.current_project['saved'] = True
        else:
            self._write_html_to_file()
        self.actionSave_Project.setEnabled(False)

    def save_project_as(self):
        io_dialog = FileIoDialog('save')
        self.current_project['project_directory'] = io_dialog.dialog()[0]
        self.current_project['project_name'] = self.current_project['project_directory'].split('/')[-1]
        os.mkdir(os.path.join(self.current_project['project_directory']))
        self._write_html_to_file()
        io_dialog.close()
        self.actionSave_Project.setEnabled(False)

    def open_item_options_dialog(self, item):
        dialog = ItemOptionsDialog(item.text(0))
        dialog.dialog()
