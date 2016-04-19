import json
import os
import sys

from PySide.QtGui import QMainWindow, QFileDialog, QTableView, QApplication, QInputDialog, QShortcut, QKeySequence
from resources.view import Ui_MainView
from src.TableModel import TableModel
from src.model import Model
from src.controller_db_credentials import DB_Credentials
from util.CSV import CSV
from util.JSON import JSON


class Controller(QMainWindow):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Ui_MainView()
        self.model = Model()

        self.view.setupUi(self)
        self.setFixedSize(800, 600)

        # Set up everything else
        self.table_view = QTableView()
        self.database_credentials = DB_Credentials()
        self.table_model = TableModel(data_in=[], header=[])

        # Just for testing purposes, loading personal config file
        data = JSON.load_config_from_json("..\\resources\\credentials.json")
        self.database_credentials.from_dict(data)
        self.database_credentials.update()
        self.session = None
        # Loading example Json -> resources/sample.json
        self.load_example_json()

        # Set up action handler
        self.setup_signals()

    def setup_signals(self):
        self.view.open.triggered.connect(self.open)
        self.view.save.triggered.connect(self.save)
        self.view.save_as.triggered.connect(self.save_as)
        self.view.actionInsert_into_databse.triggered.connect(self.into_db)
        self.view.actionSave_config.triggered.connect(self.save_config_as)
        self.view.actionLoad_Config.triggered.connect(self.load_config_from_json)
        self.view.actionNew.triggered.connect(self.new)
        self.model.tableModelChangedSignal.connect(self.model.table_model_changed)
        self.view.actionUndo.triggered.connect(self.model.undo)
        self.view.actionRedo.triggered.connect(self.model.redo)
        self.view.actionCopy.triggered.connect(
            lambda: self.model.copy(self.table_model, self.table_view.currentIndex()))
        self.view.insert_row.triggered.connect(
            lambda: self.model.insert_row(self.table_model, self.table_view.currentIndex().row(), 1))
        self.view.actionPaste.triggered.connect(
            lambda: self.model.paste(self.table_model, self.table_view.currentIndex()))
        self.view.actionCut.triggered.connect(
            lambda: self.model.cut(self.table_model, self.table_view.currentIndex()))
        self.view.actionDatabase_Credentials.triggered.connect(
            lambda: self.database_credentials.exec_())
        self.view.actionDuplicate_Row.triggered.connect(
            lambda: self.model.duplicate_row(self.table_model, self.table_view.currentIndex().row()))
        self.view.actionDelete_row.triggered.connect(
            lambda: self.model.delete_rows(self.table_model, self.table_view.currentIndex().row(), 2))

    def open(self):
        """
        Opens a file dialog to open a json file

        :return:
        """
        fname = QFileDialog.getOpenFileName(self, 'Open file...', os.getcwd(), filter="CSV-File (*.csv)")
        if not fname[0] == '':
            self.model.current_file = fname[0]
            # Let the user specify the delimiter TODO
            arr = []
            delimiter = QInputDialog.getText(self, 'Please specify delimiter', 'Delimiter: ')
            if len(delimiter[0]) > 0:
                arr = CSV.read_csv_array(fname[0], delimiter=delimiter[0])
            else:
                arr = CSV.read_csv_array(fname[0], delimiter=';')
            self.table_model.replace_all_data(data=arr[1:len(arr)], header=arr[0])
            self.table_view.setModel(self.table_model)
            self.table_model.set_data_changed_signal(self.model.tableModelChangedSignal)
            self.view.verticalLayout.addWidget(self.table_view)

    def load_example_json(self):
        """
        Loads the example json file located in resources. Only for testing purposes

        """
        fname = os.path.abspath("../resources/sample.csv")
        self.model.current_file = fname
        arr = CSV.read_csv_array(fname, delimiter=';')
        self.table_model.replace_all_data(data=arr[1:len(arr)], header=arr[0])
        self.table_view.setModel(self.table_model)
        self.table_model.set_data_changed_signal(self.model.tableModelChangedSignal)
        self.view.verticalLayout.addWidget(self.table_view)

    def save(self):
        if self.table_view.model() is not None:
            if self.model.current_file is not None:
                arr = self.table_view.model().get_data_as_2d_array()
                CSV.save_csv_2darray(arr, self.model.current_file, delimiter=';', mode='w+')
            else:
                self.save_as()
        else:
            # QErrorMessage().showMessage("Test") # immediately closes, dont know why TODO
            self.view.statusbar.showMessage("Please open a file first")

    def save_as(self):
        if self.table_view.model() is not None:
            fname = QFileDialog.getSaveFileName(self, 'Saving file...', os.getcwd())
            if not fname[0] == '':
                self.model.current_file = fname[0]
                self.save()

        else:
            # QErrorMessage().showMessage("Test") # immediately closes, dont know why TODO
            self.view.statusbar.showMessage("Please open a file first")

    def save_config_as(self):
        fname = QFileDialog.getSaveFileName(self, 'Save file...', os.getcwd(),
                                            'JavaScript Object Notation (*.json)')
        data = json.loads(json.dumps(self.database_credentials.to_dict()))
        JSON.save_config_into_json(fname[0], data)

    def load_config_from_json(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file...', os.getcwd(),
                                            'JavaScript Object Notation (*.json)')
        self.database_credentials.from_dict(JSON.load_config_from_json(fname[0]))
        self.database_credentials.update()

    def into_db(self):
        engine = None
        if self.database_credentials.hostname == '':
            self.database_credentials.exec_()
            if self.database_credentials.complete is False:
                return False
        if self.database_credentials.port != '':
            self.model.create_session(self.database_credentials.username, self.database_credentials.password,
                                      self.database_credentials.hostname, self.database_credentials.database,
                                      port=self.database_credentials.port)
        else:
            self.model.create_session(self.database_credentials.username, self.database_credentials.password,
                                      self.database_credentials.hostname, self.database_credentials.database)

        if self.table_model is not None:
            self.model.insert_into_db(self.table_model)
        else:
            self.view.statusbar.showMessage("No data to process. Please load a file first")

    def print_table(self, table):
        tables = self.session.query(table).all()
        columns = [m.key for m in tables[1].__table__.columns]
        for item in tables:
            print("------------------------------------------------------")
            for column in columns:
                print("%s: %s" % (column, item.__getattribute__(column)))
            print("------------------------------------------------------")

    def new(self):
        self.table_model.replace_all_data(data=[], header=['T', 'WV', 'WK', 'BZ', 'SPR', 'WBER', 'ABG.', 'UNG.', 'SPOE', 'FPOE', 'OEVP', 'GRUE', 'NEOS', 'WWW', 'ANDAS', 'GFW', 'SLP', 'WIFF', 'M', 'FREIE'])

    def show_window(self):
        self.show()
        self.raise_()

    def exit_handler(self):
        if self.session is not None:
            self.model.exit_handler()

app = QApplication(sys.argv)
controller = Controller()
app.aboutToQuit.connect(controller.exit_handler)
controller.show_window()
# controller.mainwindow.show()
sys.exit(app.exec_())
