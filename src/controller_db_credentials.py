from PySide.QtGui import QDialog

from resources.db_credentials_view import Ui_DatabaseCredentials


class DB_Credentials(QDialog, Ui_DatabaseCredentials):
    def __init__(self, database_dict, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.dict = database_dict

        # Setup
        self.setup()

        # Setting up signals
        self.b_save.clicked.connect(self.save)

    def setup(self):
        if self.dict["hostname"] is not None:
            self.le_hostname.setText(self.dict["hostname"])
            self.le_port.setText(self.dict["port"])
            self.le_username.setText(self.dict["username"])
            self.le_password.setText(self.dict["password"])
            self.le_database.setText(self.dict["database"])

    def save(self):
        self.dict["hostname"] = self.le_hostname.text()
        self.dict["port"] = self.le_port.text()
        self.dict["username"] = self.le_username.text()
        self.dict["password"] = self.le_password.text()
        self.dict["database"] = self.le_database.text()
        self.close()
