a = '12342342345' 
b = [1, ['a', 5, 6], 2, 3, 4, 5] 
c = {1: 'a', 2: {'a': 1, 'b': 2}, 3: 'c'} 

list_ = []
list_.append(a)
list_.append(b)
list_.append(c)

for x in list_:
    print(len(x))