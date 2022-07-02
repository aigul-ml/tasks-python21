from functools import reduce

list_ = ['Paul', 'George', 'Ringo', 'John']
result = reduce(lambda word1, word2: word1 if len(word1) > len(word2)  else word2, list_)
print(result)