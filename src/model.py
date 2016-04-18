import pyperclip
from PySide.QtCore import Signal, QObject, QModelIndex, Slot, QAbstractTableModel
from PySide.QtGui import QUndoStack
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.commands.TableModelCommand import EditCommand
from src.entities.tables import Sprengel, Partei, Stimmen


class Model(QObject):
    """
    MVC - Pattern: Represents the entities class

    """
    updateProgressSignal = Signal(int)
    tableModelChangedSignal = Signal(QAbstractTableModel, QModelIndex, str, str)
    copySignal = Signal(QAbstractTableModel, QModelIndex)

    def __init__(self):
        super(Model, self).__init__()
        self.current_file = None
        self.session = None

        # Setting up SQL relevant stuff
        self.wahl_nummer = 1

        self.undostack = QUndoStack()

    def find_indeces(self, header):
        """
        find the indeces for some items in the given header and returns them as a dictionary

        :param header: Array Header of the table model
        :return:
        """
        indeces = {'T': None, 'WV': None, 'WK': None, 'BZ': None, 'SPR': None,
                   'WBER': None, 'ABG.': None, 'UNG.': None, 'SPOE': None,
                   'FPOE': None, 'OEVP': None, 'GRUE': None, 'NEOS': None,
                   'WWW': None, 'ANDAS': None, 'GFW': None, 'SLP': None,
                   'WIFF': None, 'M': None, 'FREIE': None}
        for index, item in enumerate(header):
            indeces[item] = index
        return indeces

    def create_session(self, username, password, hostname, database, port=3306):
        """
        Creates a session to the given creadentials

        :param username: str
        :param password: str
        :param hostname: str
        :param database: str
        :param port: int Default is 3306
        """
        engine = create_engine("mysql+mysqlconnector://%s:%s@%s:%s/%s" %
                               (username, password, hostname, port, database))
        if self.session is not None:
            self.session.close()
        Session = sessionmaker(bind=engine, autoflush=False)
        self.session = Session()

    def insert_into_db(self, table_model, progress_bar):
        tmp = []
        if table_model is not None:
            arr = table_model.get_data_as_2d_array()
            # Remove spaces
            for x in range(0, len(arr)):
                for y in range(0, len(arr[x])):
                    arr[x][y] = arr[x][y].replace(" ", "")
            indeces = self.find_indeces(arr[0])
            partei_index = indeces['UNG.']+1
            parteien = self.session.query(Partei).all()

            progress = 1
            tmp = []
            for data in arr[1:]:
                print("%f" % (progress/(len(arr)-1)*100) + " %")
                # Sprengel
                sprengel = Sprengel()
                sprengel.nummer = data[indeces['SPR']]
                sprengel.wahlberechtigte = data[indeces['WBER']]
                sprengel.ungueltige = data[indeces['UNG.']]
                sprengel.abgegebene = data[indeces['ABG.']]
                sprengel.bznr = data[indeces['BZ']]
                sprengel.whnr = self.wahl_nummer
                for actual_partei_index in range(partei_index, len(arr[0])-1):
                    if data[indeces['T']] == '4' and data[indeces['WV']] == '1':
                        # Stimmen
                        stimmen = Stimmen()
                        stimmen.anzahl = data[actual_partei_index]
                        for partei in parteien:
                            if partei.bezeichnung == arr[0][actual_partei_index]:
                                stimmen.parteinr = partei.nummer
                        stimmen.spnr = sprengel.nummer
                        stimmen.bznr = data[indeces['BZ']]
                        stimmen.whnr = self.wahl_nummer
                        self.session.add(stimmen)
                    else:
                        raise Exception("Wrong CSV Format, expected Column T to be 4 and Column WV to be 1")
                self.session.add(sprengel)
                progress += 1
            try:
                print("Sending to database...")
                self.session.commit()
            except Exception as e:
                print("Could'nt insert into database, there are duplicate entries.")

    @Slot(QAbstractTableModel, QModelIndex, str, str)
    def table_model_changed(self, table_model, index, old, new):
        """
        Will be executed when data in the table model has been changed

        :param table_model: TableModel where data has been changed
        :param index: QModelIndex
        :param old: QVariant Old TableModel data
        :param new: QVariant New TableModel data
        """
        self.undostack.push(EditCommand(table_model, index, old, new))
        # print("TableModel changed at [%s, %s]" % (index.row(), index.column()))
        # print("Old Value: %s | New Value: %s" % (old, new))

    def undo(self):
        self.undostack.undo()

    def redo(self):
        self.undostack.redo()

    def copy(self, table_model, index):
        pyperclip.copy(table_model)
        print("Current index: [%s, %s]" % (index.row(), index.column()))

    def exit_handler(self):
        if self.session is not None:
            self.session.close()
