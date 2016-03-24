import csv
import os
import traceback

from PyQt5.QtWidgets import QFileDialog


class Model(object):
    """
    MVC - Pattern: Represents the entities class

    """
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.current_file = None

    def on_button_pressed(self, button):
        if str(button.objectName()) == "open":
            fname = QFileDialog.getOpenFileName(self.mainwindow, 'Open file...', os.getcwd())
        if str(button.objectName()) == "save":
            fname = QFileDialog.getSaveFileName(self.mainwindow, 'Save file...', os.getcwd())
        if str(button.objectName()) == "save_as":
            fname = QFileDialog.getSaveFileName(self.mainwindow, 'Save file as...', os.getcwd())

    def read_csv_array(self, filename, delimiter=' ', quotechar='|'):
        # TODO implement reader with 'with' statement
        reader = csv.reader(open(filename), delimiter=delimiter)
        data = []
        for row in reader:
            data.append(row)
        return data

    def save_csv_2darray(self, array, filename, delimiter=' ', mode='x'):
        # TODO implement reader with 'with' statement
        writer = csv.writer(open(filename, mode=mode), delimiter=delimiter)
        for row in array:
            writer.writerow(row)
