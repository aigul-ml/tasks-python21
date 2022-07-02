list_ = [1, 2, 3, 4, 5]
new_list = []
i = 0

while i < len(list_):
    new_list.extend([str(list_[i])])
    i += 1

print(new_list)