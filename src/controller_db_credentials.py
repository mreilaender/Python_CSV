import os

from PySide.QtGui import QDialog, QFileDialog
from resources.db_credentials_view import Ui_DatabaseCredentials


class DB_Credentials(QDialog, Ui_DatabaseCredentials):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        # Setup
        self.username = ''
        self.hostname = ''
        self.port = ''
        self.password = ''
        self.database = ''
        self.complete = False
        self.setup()
        self.l_errormsg.setStyleSheet('color: red')

        # Setting up signals
        self.b_save.clicked.connect(self.save)

    def setup(self):
        self.update()

    def save(self):
        if self.check_fields() is not False:
            self.hostname = self.le_hostname.text()
            self.hostname = self.le_hostname.text()
            self.port = self.le_port.text()
            self.username = self.le_username.text()
            self.password = self.le_password.text()
            self.database= self.le_database.text()
            self.complete = True
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

    def update(self):
        self.le_hostname.setText(self.hostname)
        self.le_port.setText(self.port)
        self.le_username.setText(self.username)
        self.le_password.setText(self.password)
        self.le_database.setText(self.database)

    def to_dict(self):
        """
        Returns all attributes of this class represented by a dictionary, where the key is the name of the variable.

        :return: dict
        """
        return {'hostname': self.hostname,
                'port': self.port,
                'username': self.username,
                'password': self.password,
                'database': self.database
                }

    def from_dict(self, data):
        """
        Updates all attributes in this class by the values of the given dictionary

        :param data: dict
        """
        if type(data) is dict:
            self.hostname = data['hostname']
            self.port = data['port']
            self.username = data['username']
            self.password = data['password']
            self.database = data['database']
        else:
            raise TypeError('incompatible types, expected dict but given type was %s' % type(data))