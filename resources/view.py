# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created: Tue Mar  1 15:15:18 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_View(object):
    def setupUi(self, View):
        View.setObjectName("View")
        View.resize(792, 480)
        self.centralwidget = QtGui.QWidget(View)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        View.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(View)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        View.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(View)
        self.statusbar.setObjectName("statusbar")
        View.setStatusBar(self.statusbar)
        self.open = QtGui.QAction(View)
        self.open.setObjectName("open")
        self.save = QtGui.QAction(View)
        self.save.setObjectName("save")
        self.save_as = QtGui.QAction(View)
        self.save_as.setObjectName("save_as")
        self.actionNew = QtGui.QAction(View)
        self.actionNew.setObjectName("actionNew")
        self.actionCopy_as = QtGui.QAction(View)
        self.actionCopy_as.setObjectName("actionCopy_as")
        self.actionExit = QtGui.QAction(View)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.open)
        self.menuFile.addAction(self.save)
        self.menuFile.addAction(self.save_as)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy_as)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(View)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), View.close)
        QtCore.QMetaObject.connectSlotsByName(View)

    def retranslateUi(self, View):
        View.setWindowTitle(QtGui.QApplication.translate("View", "asd", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setStatusTip(QtGui.QApplication.translate("View", "asdasdasd", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("View", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("View", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuWindows.setTitle(QtGui.QApplication.translate("View", "Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("View", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setText(QtGui.QApplication.translate("View", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setStatusTip(QtGui.QApplication.translate("View", "Open File", None, QtGui.QApplication.UnicodeUTF8))
        self.open.setShortcut(QtGui.QApplication.translate("View", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("View", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setStatusTip(QtGui.QApplication.translate("View", "Save file", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setShortcut(QtGui.QApplication.translate("View", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as.setText(QtGui.QApplication.translate("View", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as.setStatusTip(QtGui.QApplication.translate("View", "Save file with specific name", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as.setShortcut(QtGui.QApplication.translate("View", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("View", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setStatusTip(QtGui.QApplication.translate("View", "New file", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("View", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_as.setText(QtGui.QApplication.translate("View", "Copy CS", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy_as.setStatusTip(QtGui.QApplication.translate("View", "Copy Create Script", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("View", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setStatusTip(QtGui.QApplication.translate("View", "Exit program", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("View", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))

