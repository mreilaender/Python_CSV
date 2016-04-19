from PySide.QtGui import QUndoCommand


class EditCommand(QUndoCommand):
    """
    Handles undo/redo functionality of a QAbstractTableModel

    """
    def __init__(self, model, index, old, new):
        """
        Constructor

        :param table_model: QAbstractTableModel TableModel where data bas been changed
        :param index: QModelIndex
        :param old: QVariant Old TableModel data
        :param new: QVariant New TableModel data
        """
        super().__init__()
        self.model = model
        self.old = old
        self.new = new
        self.index = index

    def undo(self):
        self.model.setData(self.index, self.old, None)

    def redo(self):
        self.model.setData(self.index, self.new, None)


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


class DeleteRowCommand(QUndoCommand):
    """
    TODO

    """
    def __init__(self, model, row_index, row_data):
        super().__init__()
        self.model = model
        self.row_index = row_index
        self.row_data = row_data

    def undo(self):
        self.model.insertRow(self.row_index, insert_data=self.row_data)

    def redo(self):
        self.model.removeRows(self.row_index, len(self.row_data))


class DuplicateRowCommand(QUndoCommand):
    """
    TODO

    """
    def __init__(self, model, row_index, row_data):
        super().__init__()
        self.model = model
        self.row_data = row_data
        self.row_index = row_index

    def undo(self):
        self.model.removeRows(self.row_index, len(self.row_data))

    def redo(self):
        self.model.insertRow(self.row_index, insert_data=self.row_data)
