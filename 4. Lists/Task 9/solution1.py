list_ = [1, 2, 3, 4, 5]
new_list = []

for num in list_:
    if num % 2 == 0:
        new_list.append('четное')
    else:
        new_list.append('нечетное')

print(new_list)