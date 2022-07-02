list_ = [1, 2, 3, 4, 5]
new_list = []

for i in range(len(list_)):
    elem = 'четное' if not list_[i] % 2 else 'нечетное'
    new_list += [elem]

print(new_list)