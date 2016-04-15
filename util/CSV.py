import csv


class CSV:
    @staticmethod
    def read_csv_array(filename, delimiter=' ', quotechar='|'):
        # TODO implement reader with 'with' statement
        reader = csv.reader(open(filename), delimiter=delimiter)
        data = []
        for row in reader:
            data.append(row)
        return data

    @staticmethod
    def save_csv_2darray(array, filename, delimiter=' ', mode='x'):
        # TODO implement reader with 'with' statement
        writer = csv.writer(open(filename, mode=mode), delimiter=delimiter)
        for row in array:
            writer.writerow(row)
