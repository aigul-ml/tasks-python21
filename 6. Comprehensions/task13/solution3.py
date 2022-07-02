string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

list_ = [num for num in string_.split() if num.isnumeric()]

print(list_)