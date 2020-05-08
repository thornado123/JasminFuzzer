import os
import json
from jasminDistribution import Instructions

class JsonSerializer:
    def __init__(self):
        self.json_path = json_path = os.getcwd()+"/json/"

    def json_to_obj(self, json_file, class_ref, *init_args):
        obj = class_ref(*init_args)
        FILE = self.json_path + json_file

        with open(FILE, 'r') as f:
            obj_dict = (json.load(f))

        obj.__dict__ = obj_dict

        return obj

    # NOT IN USE
    def obj_to_json(self, json_file, obj):
        data = obj.__dict__
        FILE = self.json_path + json_file
        with open(FILE, 'w') as f:
            json.dump(data, f, indent = 4)

    def dist_to_json(self, fields):
        pass
    
json_file = 'test.json'

JS = JsonSerializer()
ins = Instructions(42)
JS.obj_to_json(json_file, ins)


obj = JS.json_to_obj(json_file, Instructions, 2)

print(ins.__dict__ == obj.__dict__)
print(ins.__dict__)
print()
print(obj.__dict__)
A = [obj.__dict__[key] == val for key, val in ins.__dict__.items()]
print(A)