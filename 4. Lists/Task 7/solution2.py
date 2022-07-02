inp1 = input().replace(',', '')

list_ = []

for num in inp1:
    list_.append(num)
    
tuple_ = tuple(list_)

print(list_)
print(tuple_)