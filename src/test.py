import json
import jasminDistribution as JD
from jsonSerializer import K
FILE = 'json/test.json'


data = JD.Instructions(2)

with open(FILE, 'w') as f:
    json.dump(data.__dict__, f, indent = 4)


with open(FILE, 'r') as f:
    o = json.load(f)
print(o)

