import json

str1 = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

json_str = json.loads(str1)
print(json_str)
print(type(json_str))

with open('json.data', 'w') as f:
    f.write(str1)