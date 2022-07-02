from math import ceil

name_of_list = ['Helloworld!']
string = name_of_list[0]

mid = ceil(len(string) / 2)
result = list(string[mid:] + string[:mid])

print(result)