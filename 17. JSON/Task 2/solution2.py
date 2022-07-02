import json

file = open('task2.json')
json_obj = file.read()
python_obj = json.loads(json_obj)

file.close()