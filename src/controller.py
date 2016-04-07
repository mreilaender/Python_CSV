import json
import os
import sys

from PySide.QtGui import QWidget, QMainWindow, QFileDialog, QTableView, QApplication, QErrorMessage, QInputDialog
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from resources.view import Ui_MainView
from src.TableModel import TableModel
from src.model import Model
from src.controller_db_credentials import DB_Credentials
from src.entities.tables import Partei


class Controller(QWidget):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Ui_MainView()
        self.mainwindow = QMainWindow()
        self.model = Model(self.mainwindow)

        self.view.setupUi(self.mainwindow)
        self.setFixedSize(620, 250)

        # Set up action handler
        self.setup_signals()

        # Set up everything else
        self.table_view = QTableView()
        self.indeces = {'T': None, 'WV': None, 'WK': None, 'BZ': None, 'SPR': None,
                        'WBER': None, ' ABG.': None, 'UNG.': None, 'SPOE': None,
                        'FPOE': None, 'OEVP': None, 'GRUE': None, 'NEOS': None,
                        'WWW': None, 'ANDAS': None, 'GFW': None, 'SLP': None,
                        'WIFF': None, 'M': None, 'FREIE': None}
        self.database_credentials = DB_Credentials()

        # Just for testing purposes, loading personal config file
        data = self.model.load_config_from_json(
            "..\\resources\\credentials.json")
        self.database_credentials.from_dict(data)
        self.database_credentials.update()
        self.session = None

    def setup_signals(self):
        self.view.open.triggered.connect(self.open)
        self.view.insert_row.triggered.connect(self.insert_row)
        self.view.save.triggered.connect(self.save)
        self.view.save_as.triggered.connect(self.save_as)
        self.view.actionInsert_into_databse.triggered.connect(self.into_db)
        self.view.actionSave_config.triggered.connect(self.save_config_as)
        self.view.actionLoad_Config.triggered.connect(self.load_config_from_json)
        self.view.actionDatabase_Credentials.triggered.connect(lambda: self.database_credentials.exec_())
        # self.view.open.triggered.connect(lambda: self.entities.on_button_pressed(self.view.open))
        # self.view.save.triggered.connect(lambda: self.entities.on_button_pressed(self.view.save))
        # self.view.save_as.triggered.connect(lambda: self.entities.on_button_pressed(self.view.save_as))

    def open(self):
        fname = QFileDialog.getOpenFileName(self.mainwindow, 'Open file...', os.getcwd())
        if not fname[0] == '':
            self.model.current_file = fname[0]
            # Let the user specify the delimiter TODO
            # delimiter = QInputDialog.getText(self, 'Please specify delimiter', 'Delimiter: ')
            arr = self.model.read_csv_array(fname[0], delimiter=';')
            # Creating table entities,
            #   arr[0] -> header
            #   arr[1:len(arr)] -> actual data
            table_model = TableModel(arr[1:len(arr)], arr[0])
            self.table_view.setModel(table_model)
            self.view.verticalLayout.addWidget(self.table_view)

    def save(self):
        if self.table_view.model() is not None:
            if self.model.current_file is not None:
                arr = self.table_view.model().get_data_as_2d_array()
                self.model.save_csv_2darray(arr, self.model.current_file, delimiter=';', mode='w')
            else:
                self.save_as()
        else:
            # QErrorMessage().showMessage("Test") # immediately closes, dont know why TODO
            self.view.statusbar.showMessage("Please open a file first")

    def save_as(self):
        if self.table_view.model() is not None:
            fname = QFileDialog.getSaveFileName(self.mainwindow, 'Saving file...', os.getcwd())
            if not fname[0] == '':
                self.model.current_file = fname[0]
        else:
            # QErrorMessage().showMessage("Test") # immediately closes, dont know why TODO
            self.view.statusbar.showMessage("Please open a file first")

    def save_config_as(self):
        fname = QFileDialog.getSaveFileName(self.mainwindow, 'Save file...', os.getcwd(),
                                            'JavaScript Object Notation (*.json)')
        data = json.loads(json.dumps(self.database_credentials.to_dict()))
        self.model.save_config_into_json(fname[0], data)

    def load_config_from_json(self):
        fname = QFileDialog.getOpenFileName(self.mainwindow, 'Open file...', os.getcwd(),
                                            'JavaScript Object Notation (*.json)')
        self.database_credentials.from_dict(self.model.load_config_from_json(fname[0]))
        self.database_credentials.update()

    def insert_row(self):
        """
        Inserts a row at below the row of the currently focused element

        """
        self.table_view.model().insertRow(self.table_view.currentIndex().row()+1)

    def into_db(self):
        engine = None
        if self.database_credentials.hostname == '':
            self.database_credentials.exec_()
            if self.database_credentials.complete is False:
                return False
        if self.database_credentials.port != '':
            engine = create_engine("mysql+mysqlconnector://%s:%s@%s:%s/%s" %
                                   (self.database_credentials.username,
                                    self.database_credentials.password,
                                    self.database_credentials.hostname,
                                    self.database_credentials.port,
                                    self.database_credentials.database)
                                   )
        else:
            engine = create_engine("mysql+mysqlconnector://%s:%s@%s/%s" %
                                   (self.database_credentials.username,
                                    self.database_credentials.password,
                                    self.database_credentials.hostname,
                                    self.database_credentials.database)
                                   )
        Session = sessionmaker(bind=engine)
        self.session = Session()

        table_model = self.table_view.model()
        if table_model is not None:
            arr = table_model.get_data_as_2d_array()[0]
            for item in arr:
                item = item.replace(" ", "")
                # TODO in db eintragen

            """
            parteien = self.session.query(Partei).all()
            for partei in parteien:
                print(partei.bezeichnung)
            """
        else:
            self.view.statusbar.showMessage("No data to process. Please load a file first")

    def exit_handler(self):
        if self.session is not None:
            self.session.close()

app = QApplication(sys.argv)
controller = Controller()
app.aboutToQuit.connect(controller.exit_handler)
controller.mainwindow.show()
sys.exit(app.exec_())
