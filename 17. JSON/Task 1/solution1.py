import json

with open('task1.json') as file1:
    python_obj = json.load(file1)
    
    file2 = open('task1.py', 'w')
    file2.write(str(python_obj))

    file2.close()