import math

class Math:
    def __init__(self, value):
        self.value = value
    
    def get_factorial(self):
        fact = math.factorial(self.value)
        return fact

    def get_sum(self):
        num_list = list(map(int, str(self.value)))
        result = sum(num_list)
        return result

    def get_mul_table(self):
        result = ''
        num_list = list(range(1, 11))
        for num in num_list:
            line = self.value * num
            result += f'{self.value}x{num}={line}\n'
        return result

num = Math(11)

print(num.get_factorial())
print(num.get_sum())
print(num.get_mul_table())
