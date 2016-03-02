import csv
import os
import traceback

import itertools
from PyQt5.QtWidgets import QFileDialog


class Model(object):
    """
    MVC - Pattern: Represents the model class

    """
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def on_button_pressed(self, button):
        if str(button.objectName()) == "open":
            fname = QFileDialog.getOpenFileName(self.mainwindow, 'Open file...', os.getcwd())
        if str(button.objectName()) == "save":
            fname = QFileDialog.getSaveFileName(self.mainwindow, 'Save file...', os.getcwd())
        if str(button.objectName()) == "save_as":
            fname = QFileDialog.getSaveFileName(self.mainwindow, 'Save file as...', os.getcwd())

    def read_csv_array(self, filename, delimiter=' ', quotechar='|'):
        reader = csv.reader(open(filename), delimiter=delimiter)
        data = []
        for row in reader:
            data.append(row)
        return data
