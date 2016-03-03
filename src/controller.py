import os
import sys

from PySide.QtGui import QWidget, QMainWindow, QFileDialog, QTableView, QApplication, QErrorMessage, QInputDialog
from resources.view import Ui_View
from src.TableModel import TableModel
from src.model import Model


class Controller(QWidget):
    """
    MVC Pattern: Represents the controller class

    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.view = Ui_View()
        self.mainwindow = QMainWindow()
        self.model = Model(self.mainwindow)

        self.view.setupUi(self.mainwindow)
        self.setFixedSize(620, 250)

        # Set up action handler
        self.setup_signals()

        # Set up everything else
        self.table_view = QTableView()

    def setup_signals(self):
        self.view.open.triggered.connect(self.open)
        self.view.insert_row.triggered.connect(self.insert_row)
        self.view.save.triggered.connect(self.save)
        self.view.save_as.triggered.connect(self.save_as)
        # self.view.open.triggered.connect(lambda: self.model.on_button_pressed(self.view.open))
        # self.view.save.triggered.connect(lambda: self.model.on_button_pressed(self.view.save))
        # self.view.save_as.triggered.connect(lambda: self.model.on_button_pressed(self.view.save_as))

    def open(self):
        fname = QFileDialog.getOpenFileName(self.mainwindow, 'Open file...', os.getcwd())
        if not fname[0] == '':
            self.model.current_file = fname[0]
            # Let the user specify the delimiter TODO
            # delimiter = QInputDialog.getText(self, 'Please specify delimiter', 'Delimiter: ')
            arr = self.model.read_csv_array(fname[0], delimiter=';')
            # Creating table model,
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

    def insert_row(self):
        """
        Inserts a row at below the row of the currently focused element

        """
        self.table_view.model().insertRow(self.table_view.currentIndex().row()+1)
        # print(self.table_view.currentIndex().row())

app = QApplication(sys.argv)
controller = Controller()
controller.mainwindow.show()
sys.exit(app.exec_())
