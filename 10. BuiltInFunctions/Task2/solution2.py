list_ = [1, 5, -9, 6, -4]

def func(ls):
    result = []
    for num in ls:
        if num > 3:
            result.append(num)
        else:
            pass

    if len(result) < len(ls):
        return False
    else:
        return True

print(func(list_))