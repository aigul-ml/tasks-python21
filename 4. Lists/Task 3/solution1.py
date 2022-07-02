name_of_list = ['Helloworld!']

string = name_of_list[0]
length = len(string)

if length % 2 == 0:
    result = list(string[length // 2:] + string[:length // 2])
else:
    result = list(string[length // 2 + 1:] + string[:length // 2 + 1])

print(result)