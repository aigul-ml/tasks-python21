class Salary:
    percent = 8

    def __init__(self, salary, experience):
        self.salary = salary
        self.experience = experience

    def count_percent(self):
        tax_per_month = self.salary / 100 * self.percent
        result = self.experience * tax_per_month
        return result

obj = Salary(10000, 10)

print(obj.count_percent())