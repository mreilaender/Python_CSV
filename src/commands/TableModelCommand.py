from PySide.QtGui import QUndoCommand


class EditCommand(QUndoCommand):
    """
    Handles undo/redo functionality of a QAbstractTableModel

    """
    def __init__(self, table_model, index, old, new):
        """
        Constructor

        :param table_model: QAbstractTableModel TableModel where data bas been changed
        :param index: QModelIndex
        :param old: QVariant Old TableModel data
        :param new: QVariant New TableModel data
        """
        super().__init__()
        self.table_model = table_model
        self.old = old
        self.new = new
        self.index = index

    def undo(self):
        self.table_model.setData(self.index, self.old, None)

    def redo(self):
        self.table_model.setData(self.index, self.new, None)


class InsertRowCommand(QUndoCommand):
    """
    Handles undo/redo if inserting a row functionality of a QAbstractTableModel
    """
    def __init__(self, model, row, count):
        super().__init__()
        self.model = model
        self.row = row
        self.count = count

    def undo(self):
        self.model.removeRows(self.row, self.count)

    def redo(self):
        self.model.insertRow(self.row, self.count)
