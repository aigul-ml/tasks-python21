n = int(input())

dict_ = {num: num ** 2 for num in range(1, 501) if num % n == 0}

print(dict_)