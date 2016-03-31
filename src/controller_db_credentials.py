import os

from PySide.QtGui import QDialog, QFileDialog
from resources.db_credentials_view import Ui_DatabaseCredentials


class DB_Credentials(QDialog, Ui_DatabaseCredentials):
    def __init__(self, database_dict, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        self.dict = database_dict

        # Setup
        self.setup()
        self.l_errormsg.setStyleSheet('color: red')

        # Setting up signals
        self.b_save.clicked.connect(self.save)

    def setup(self):
        if self.dict['hostname'] is not None:
            self.le_hostname.setText(self.dict['hostname'])
            self.le_port.setText(self.dict['port'])
            self.le_username.setText(self.dict['username'])
            self.le_password.setText(self.dict['password'])
            self.le_database.setText(self.dict['database'])

    def save(self):
        if self.check_fields() is not False:
            self.dict['hostname'] = self.le_hostname.text()
            self.dict['port'] = self.le_port.text()
            self.dict['username'] = self.le_username.text()
            self.dict['password'] = self.le_password.text()
            self.dict['database'] = self.le_database.text()
            self.dict['complete'] = True
            self.close()

    def check_fields(self):
        if self.le_hostname.text() == '':
            self.l_errormsg.setText("You have to specify a hostname")
            return False
        if self.le_username.text() == '':
            self.l_errormsg.setText("You have to specify a username")
            return False
        if self.le_database.text() == '':
            self.l_errormsg.setText("You have to specify a database")
            return False

    def showEvent(self, event):
        self.setup()
