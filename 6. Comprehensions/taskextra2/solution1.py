dict_ = {1: 'Hello', 2: 'World', 3: 'John'}

new_dict = {key: len(val) if key % 2 == 0 else len(val) ** 3 for key, val in dict_.items()}

print(new_dict)