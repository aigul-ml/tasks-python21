string = "pythonist" 
dict_ = {}

for letter in string:
    dict_.update({letter: string.count(letter)})

print(dict_)