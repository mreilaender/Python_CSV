# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database_credentials.ui'
#
# Created: Thu Mar 24 21:53:14 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DatabaseCredentials(object):
    def setupUi(self, DatabaseCredentials):
        DatabaseCredentials.setObjectName("DatabaseCredentials")
        DatabaseCredentials.resize(340, 227)
        self.verticalLayout = QtGui.QVBoxLayout(DatabaseCredentials)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.l_password = QtGui.QLabel(DatabaseCredentials)
        self.l_password.setObjectName("l_password")
        self.gridLayout.addWidget(self.l_password, 3, 2, 1, 1)
        self.l_port = QtGui.QLabel(DatabaseCredentials)
        self.l_port.setObjectName("l_port")
        self.gridLayout.addWidget(self.l_port, 1, 2, 1, 1)
        self.le_password = QtGui.QLineEdit(DatabaseCredentials)
        self.le_password.setAcceptDrops(True)
        self.le_password.setEchoMode(QtGui.QLineEdit.Password)
        self.le_password.setObjectName("le_password")
        self.gridLayout.addWidget(self.le_password, 3, 3, 1, 1)
        self.le_port = QtGui.QLineEdit(DatabaseCredentials)
        self.le_port.setObjectName("le_port")
        self.gridLayout.addWidget(self.le_port, 1, 3, 1, 1)
        self.le_database = QtGui.QLineEdit(DatabaseCredentials)
        self.le_database.setObjectName("le_database")
        self.gridLayout.addWidget(self.le_database, 4, 1, 1, 1)
        self.l_database = QtGui.QLabel(DatabaseCredentials)
        self.l_database.setObjectName("l_database")
        self.gridLayout.addWidget(self.l_database, 4, 0, 1, 1)
        self.le_username = QtGui.QLineEdit(DatabaseCredentials)
        self.le_username.setObjectName("le_username")
        self.gridLayout.addWidget(self.le_username, 3, 1, 1, 1)
        self.l_hostname = QtGui.QLabel(DatabaseCredentials)
        self.l_hostname.setObjectName("l_hostname")
        self.gridLayout.addWidget(self.l_hostname, 1, 0, 1, 1)
        self.l_username = QtGui.QLabel(DatabaseCredentials)
        self.l_username.setObjectName("l_username")
        self.gridLayout.addWidget(self.l_username, 3, 0, 1, 1)
        self.le_hostname = QtGui.QLineEdit(DatabaseCredentials)
        self.le_hostname.setObjectName("le_hostname")
        self.gridLayout.addWidget(self.le_hostname, 1, 1, 1, 1)
        self.l_errormsg = QtGui.QLabel(DatabaseCredentials)
        self.l_errormsg.setEnabled(True)
        self.l_errormsg.setMaximumSize(QtCore.QSize(16777215, 20))
        self.l_errormsg.setText("")
        self.l_errormsg.setTextFormat(QtCore.Qt.AutoText)
        self.l_errormsg.setObjectName("l_errormsg")
        self.gridLayout.addWidget(self.l_errormsg, 5, 0, 1, 4)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b_save = QtGui.QPushButton(DatabaseCredentials)
        self.b_save.setObjectName("b_save")
        self.horizontalLayout_2.addWidget(self.b_save)
        self.b_cancel = QtGui.QPushButton(DatabaseCredentials)
        self.b_cancel.setObjectName("b_cancel")
        self.horizontalLayout_2.addWidget(self.b_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(DatabaseCredentials)
        QtCore.QObject.connect(self.b_cancel, QtCore.SIGNAL("clicked()"), DatabaseCredentials.close)
        QtCore.QMetaObject.connectSlotsByName(DatabaseCredentials)

    def retranslateUi(self, DatabaseCredentials):
        DatabaseCredentials.setWindowTitle(QtGui.QApplication.translate("DatabaseCredentials", "Database credentials", None, QtGui.QApplication.UnicodeUTF8))
        self.l_password.setText(QtGui.QApplication.translate("DatabaseCredentials", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.l_port.setText(QtGui.QApplication.translate("DatabaseCredentials", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.l_database.setText(QtGui.QApplication.translate("DatabaseCredentials", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.l_hostname.setText(QtGui.QApplication.translate("DatabaseCredentials", "Hostname", None, QtGui.QApplication.UnicodeUTF8))
        self.l_username.setText(QtGui.QApplication.translate("DatabaseCredentials", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.b_save.setText(QtGui.QApplication.translate("DatabaseCredentials", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.b_cancel.setText(QtGui.QApplication.translate("DatabaseCredentials", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

