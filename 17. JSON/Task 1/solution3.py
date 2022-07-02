import json

with open('task1.json') as file1:
    python_obj = json.load(file1)
    
    with open('task1.py', 'w') as file2:
        file2.write(str(python_obj))