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
        self.table_model.layoutAboutToBeChanged.emit()
        self.table_model.setData(self.index, self.old, None)
        self.table_model.layoutChanged.emit()

    def redo(self):
        self.table_model.layoutAboutToBeChanged.emit()
        self.table_model.setData(self.index, self.new, None)
        self.table_model.layoutChanged.emit()
