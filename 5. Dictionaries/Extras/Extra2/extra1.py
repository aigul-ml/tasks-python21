string = "pythonist" 
dict_ = {}
for letter in string:
    dict_[letter] = dict_.get(letter, 0) + 1
print(dict_)