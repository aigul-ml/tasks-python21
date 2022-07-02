import json

file1 = open('task1.json')
python_obj = json.load(file1)
file1.close()

file2 = open('task1.py', 'w')
file2.write(str(python_obj))
file2.close()