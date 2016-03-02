from PySide.QtCore import QAbstractTableModel, Qt


class TableModel(QAbstractTableModel):
    def __init__(self, data_in, header):
        super().__init__()
        self.data_in = data_in
        self.header = header

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.data_in[index.row()][index.column()]

    def rowCount(self, parent):
        return len(self.data_in)

    def columnCount(self, parent):
        return len(self.data_in[0])

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

