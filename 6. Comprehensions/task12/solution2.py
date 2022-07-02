dict_ = {'first': 1, 'second': 2, 'third': 3}

a = {key: 'even' if dict_[key] % 2 == 0 else 'odd' for key in dict_.keys()}

print(a)