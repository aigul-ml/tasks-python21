n = int(input())

dict_ = {num: num * num for num in range(1, 501) if not num % n}

print(dict_)