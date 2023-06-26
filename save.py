import json
import os

import logger


class SaveGame:
    def __init__(self, filename, data={}):
        self.logger = logger.Logger()
        self.filename = filename

        if not os.path.isfile(filename):
            with open(filename, 'w') as file:
                json.dump(data, file)

    def save(self, data):
        with open(self.filename, 'w') as f:
            json.dump(data, f)

    def load_all(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def append_item_to_list(self, value):
        list_obj = []
        with open(self.filename) as fp:
            list_obj = json.load(fp)
        list_obj.append(value)
        with open(self.filename, 'w') as json_file:
            json.dump(list_obj, json_file,
                      indent=4,
                      separators=(',', ': '))

    def delete_item_from_list(self, value):
        list_obj = []
        with open(self.filename) as fp:
            list_obj = json.load(fp)
        for obj in list_obj:
            if obj["id"] == value:
                list_obj.remove(obj)
        with open(self.filename, 'w') as json_file:
            json.dump(list_obj, json_file,
                      indent=4,
                      separators=(',', ': '))

    def load_item_from_list(self, value):
        list_obj = []
        with open(self.filename) as fp:
            list_obj = json.load(fp)
        for obj in list_obj:
            if obj["id"] == value:
                return obj
