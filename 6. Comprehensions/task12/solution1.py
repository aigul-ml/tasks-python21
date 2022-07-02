dict_ = {'first': 1, 'second': 2, 'third': 3}

a = {key: 'even' if val % 2 == 0 else 'odd' for key, val in dict_.items()}

print(a)