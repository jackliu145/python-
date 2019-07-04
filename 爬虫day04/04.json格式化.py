import json

with open('json.data', 'r') as r:
    with open('formart_json.data', 'w') as w:
        json_str = json.loads(r.read())
        print(json_str)
        print(type(json_str))
        w.write(json.dumps(json_str, indent='\n'))