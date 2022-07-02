list_ = [1, 2, 3, 4, 5]
new_list = []
i = 0

while i < len(list_):
    if list_[i] % 2 == 0:
        new_list.append('четное')
        i += 1
        continue
    new_list.append('нечетное')
    i += 1

print(new_list)