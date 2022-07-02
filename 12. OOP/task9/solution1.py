class Math:
    def __init__(self, value):
        self.value = value

    def get_factorial(self):
        count = 1
        list_ = [num for num in range(1, self.value + 1)]
        for num in list_:
            count *= num
        return count
        
    def get_sum(self):
        sum_ = list(str(self.value))
        count = 0
        for x in sum_:
            count += int(x)
        return count

    def get_mul_table(self):
        list_ = []
        for num in range(1, 11):
            result = num * self.value
            list_.append(f'{self.value}x{num}={result}\n')
        return ''.join(list_)

        
a = Math(25)

print(a.get_factorial())
print(a.get_sum())
print(a.get_mul_table())