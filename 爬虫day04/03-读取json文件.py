import json

with open('json.data', 'r') as f:
    str = f.read()
    j = json.loads(str)
    print(j)
    print(type(j))