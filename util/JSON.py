import json


class JSON:
    @staticmethod
    def save_config_into_json(filename, data):
        with open(filename, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def load_config_from_json(filename):
        with open(filename, 'r') as file:
            return json.load(file)