import csv
import json


class Model(object):
    """
    MVC - Pattern: Represents the entities class

    """
    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.current_file = None

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

    def save_config_into_json(self, filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_config_from_json(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

    def find_indeces(self, header):
        """
        find the indeces for some items in the given header and returns them as a dictionary

        :param header: Array Header of the table model
        :return:
        """
        indeces = {'T': None, 'WV': None, 'WK': None, 'BZ': None, 'SPR': None,
                        'WBER': None, 'ABG.': None, 'UNG.': None, 'SPOE': None,
                        'FPOE': None, 'OEVP': None, 'GRUE': None, 'NEOS': None,
                        'WWW': None, 'ANDAS': None, 'GFW': None, 'SLP': None,
                        'WIFF': None, 'M': None, 'FREIE': None}
        for index, item in enumerate(header):
            indeces[item] = index
        return indeces