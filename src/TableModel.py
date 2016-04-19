from PySide.QtCore import QAbstractTableModel, Qt, QModelIndex


class TableModel(QAbstractTableModel):

    def __init__(self, data_in, header):
        super().__init__()
        self.data_in = data_in
        self.header = header
        self.data_changed_signal = None
        self.copy_signal = None

    def set_data_changed_signal(self, signal):
        """
        Sets the signal to be emited when the data has changed

        :param signal: Signal
        """
        self.data_changed_signal = signal

    def replace_all_data(self, data=None, header=None):
        """
        Replaces header and data (if specified)

        :param data: 2D Array
        :param header: Array
        """
        self.layoutAboutToBeChanged.emit()
        if data is not None:
            self.data_in = data
        if header is not None:
            self.header = header
        self.layoutChanged.emit()

    def get_row(self, row_index):
        """
        Returns a row at the given row index as an array

        :param row_index: int Index of the row
        :return: Array
        """
        return self.data_in[row_index]

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.data_in[index.row()][index.column()]

    def rowCount(self, parent):
        return len(self.data_in)

    def columnCount(self, parent):
        if len(self.data_in) > 0:
            return len(self.data_in[0])
        return 0

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

    def flags(self, *args, **kwargs):
        return Qt.ItemIsEditable | Qt.ItemIsSelectable | Qt.ItemIsEnabled

    def setData(self, index, value, role):
        self.layoutAboutToBeChanged.emit()
        if role is not None:
            old = self.data_in[index.row()][index.column()]
            self.data_changed_signal.emit(self, index, old, value)
        self.data_in[index.row()][index.column()] = value
        self.layoutChanged.emit()
        return True

    def insertRow(self, row, rows=1, insert_data=""):
        """
        Inserts a row after a given row index

        :param insert_data: str or list Placeholder to be inserted in every column
        :param row: Int Row where the row will be inserted
        :param rows: Number of rows that will be implemented
        """
        self.layoutAboutToBeChanged.emit()
        if type(insert_data) is list:
            if rows != 1 and len(insert_data) != rows:
                raise IndexError("Length of insert_data must be equal to rows")
            for element in insert_data:
                self.data_in.insert(row, element)
                row += 1
        else:
            # Filling array with empty strings
            for tmp in range(rows):
                self.data_in.insert(row, [insert_data for x in range(0, len(self.header))])
        self.layoutChanged.emit()

    def duplicateRow(self, row_index, parent=QModelIndex()):
        self.layoutAboutToBeChanged.emit()
        self.data_in.insert(row_index, self.data_in[row_index])
        self.layoutChanged.emit()

    def removeRows(self, row, count, parent=QModelIndex()):
        self.layoutAboutToBeChanged.emit()
        del self.data_in[row:count]
        self.layoutChanged.emit()

    def get_rows(self, row_index, count=1):
        return self.data_in[row_index:row_index+count]

    def get_data_as_2d_array(self):
        table_data = self.data_in
        table_header = self.header
        arr = [table_header]
        [arr.append(table_data[x]) for x in range(0, len(table_data))]
        return arr
