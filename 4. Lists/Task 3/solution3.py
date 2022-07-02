name_of_list = ['Helloworld!']

length = len(name_of_list[0]) + 1
string = name_of_list[0]
string = string[length // 2:] + string[:length // 2]
result = list(string)

print(result)