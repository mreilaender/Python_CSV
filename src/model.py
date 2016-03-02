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
        arr = []
        # Creating 2d array (columns and rows the same as the csv) and fill it with 0
        with open(filename, newline='\n') as csvfile:
            tmp = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            rows, columns = 0, 0
            for row in tmp:
                rows += 1
                columns = len(row)
            arr = [[0 for x in range(columns)] for x in range(rows)]
            del tmp

        # Filling the 2d array created above
        with open(filename, newline='\n') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=delimiter, quotechar=quotechar)
            curr_row, curr_column = 0, 0
            for row in spamreader:
                curr_column = 0
                for element in row:
                    arr[curr_row][curr_column] = element.strip()
                    curr_column += 1
                curr_row += 1
        return arr
