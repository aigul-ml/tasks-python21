import json

with open('task2.json') as file:
    json_obj = file.read()
    python_obj = json.loads(json_obj)