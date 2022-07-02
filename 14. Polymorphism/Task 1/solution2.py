a = '12342342345' 
b = [1, ['a', 5, 6], 2, 3, 4, 5] 
c = {1: 'a', 2: {'a': 1, 'b': 2}, 3: 'c'} 

list_ = [a, b, c]
i = 0

while i < len(list_):
    print(len(list_[i]))
    i += 1