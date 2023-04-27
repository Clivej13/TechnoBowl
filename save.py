import json
import logger


class SaveGame:
    def __init__(self, filename):
        self.Logger = logger.Logger()
        self.filename = filename

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_all(self, value_key):
        with open(self.filename, 'r') as f:
            return json.load(f)[value_key]

    def append(self, value, value_key):
        list_obj = []
        with open(self.filename) as fp:
            list_obj = json.load(fp)[value_key]
        list_obj.append(value)
        with open(self.filename, 'w') as json_file:
            json.dump({value_key: list_obj}, json_file,
                      indent=4,
                      separators=(',', ': '))

    def delete(self, value, value_key):
        list_obj = []
        with open(self.filename) as fp:
            list_obj = json.load(fp)[value_key]
        for obj in list_obj:
            if obj["id"] == value:
                list_obj.remove(obj)
        with open(self.filename, 'w') as json_file:
            json.dump({value_key: list_obj}, json_file,
                      indent=4,
                      separators=(',', ': '))

    def load(self, value, value_key):
        list_obj = []
        with open(self.filename) as fp:
            list_obj = json.load(fp)[value_key]
        for obj in list_obj:
            if obj["id"] == value:
                return obj
