list_ = [1, 1, 3]
i = 0
answer = False

while i < len(list_):
    if list_.count(list_[i]) != 1:
        answer = True
        break
    i += 1

print('yes' if answer else 'ERROR')