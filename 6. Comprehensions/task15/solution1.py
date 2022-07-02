my_dict = {
    'first': {'a': 1}, 
    'second': {'b': 2}
}

dict_ = {key1: val2 for key1, val1 in my_dict.items() for val2 in val1.values()}

print(dict_)