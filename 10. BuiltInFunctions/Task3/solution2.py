list_ = [5, 8, 4, 6, -1]

def func(ls):
    new_list = []
    for num in list_:
        if num > 0:
            new_list.append(num)
        else:
            pass

    if len(new_list) < len(ls):
        return False
    else:
        return True

print(func(list_))