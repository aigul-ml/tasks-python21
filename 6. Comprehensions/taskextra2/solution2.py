dict_ = {1: 'Hello', 2: 'World', 3: 'John'}

new_dict = {key: len(dict_[key]) if not key % 2 else pow(len(dict_[key]), 3) for key in dict_.keys()}

print(new_dict)