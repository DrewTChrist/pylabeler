from PyQt5.QtWidgets import QApplication
from pylabeler.ui.main_window import MainWindow
from pylabeler.html_model import HtmlModel
from pylabeler.ui import icons
import qtawesome
from qt_material import apply_stylesheet
import os
import sys


class Application:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self._app.setWindowIcon(qtawesome.icon(icons.barcode))
        apply_stylesheet(self._app, 'dark_teal.xml')
        self._main_window = MainWindow()
        self.model = HtmlModel()
        self.initialize_signals()
        self._main_window.show()

        self.current_project = {
            "project_name": None,
            "project_directory": None,
            "data_source": None,
            "saved": False,
        }

        sys.exit(self._app.exec_())

    def initialize_signals(self):
        self.model.dataChanged.connect(
            lambda: self._main_window.html_model_event(self.model))
        self._main_window.htmlTextBox.textChanged.connect(
            lambda: self._main_window.text_editor_event(self.model))
        self._main_window.actionNew_Project.triggered.connect(self.new_project)
        self._main_window.actionOpen_Project.triggered.connect(
            self.open_project)
        self._main_window.actionClose_Project.triggered.connect(
            self.close_project)
        self._main_window.actionSave_Project.triggered.connect(
            self.save_project)
        self._main_window.actionSave_As.triggered.connect(self.save_project_as)

    def new_project(self):
        self.model.load_base()
        self.current_project = {
            "project_name": None,
            "project_directory": None,
            "data_source": None,
            "saved": False,
        }
        self._main_window.enable_project_ui()

    def close_project(self):
        self.current_project = {
            "project_name": None,
            "project_directory": None,
            "data_source": None,
            "saved": False,
        }
        self.model.set_html("")
        self._main_window.disable_project_ui()

    def save_project(self):
        if not self.current_project["saved"]:
            self.save_project_as()
        else:
            self._write_html_to_file()
            self._main_window.ui_element_set_enabled(
                'actionSave_Project', False)

    def save_project_as(self):
        directory = self._main_window.file_io_dialog("save")[0]
        if directory:
            self.current_project["project_directory"] = directory
            self.current_project["project_name"] = self.current_project["project_directory"].split(
                "/")[-1]
            os.mkdir(os.path.join(
                str(self.current_project["project_directory"])))
            self._write_html_to_file()
            self.current_project["saved"] = True
            self._main_window.ui_element_set_enabled(
                'actionSave_Project', False)

    def open_project(self):
        self.current_project['project_directory'] = self._main_window.file_io_dialog(
            "open")
        label_path = os.path.join(
            str(self.current_project["project_directory"]), "label.html"
        )
        if os.path.exists(str(self.current_project["project_directory"])) and os.path.exists(
                label_path
        ):
            try:
                with open(label_path, "r") as file:
                    self.model.set_html(file.read())
                    file.close()
            except Exception as e:
                print(e)

            self.current_project["saved"] = True
            self._main_window.enable_project_ui()
            self._main_window.ui_element_set_enabled(
                'actionSave_Project', False)

    def _write_html_to_file(self):
        label_path = os.path.join(
            str(self.current_project["project_directory"]), "label.html")
        with open(label_path, "w") as file:
            file.write(self.model.html)
        file.close()
