class MyString(str):
    def __init__(self, value):
        self.value = value
    
    def append(self, string):
        self.value += string

    def pop(self):
        string = self.value
        self.value = self.value[:-1]
        return string[-1]

    def __str__(self):
        return self.value

example = MyString('String')
example.append('hello')
print(example) 
print(example.pop()) 
print(example) 