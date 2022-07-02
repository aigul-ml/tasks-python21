class Person:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_info(self):
        return f'Привет, меня зовут {self.name} {self.last_name}'

class Employee(Person):
    def __init__(self, name, last_name, work, status):
        super().__init__(name, last_name)
        self.work = work
        self.status = status

    def get_info(self):
        person_info = super().get_info()
        return f'{person_info}, я работаю в компании {self.work} на должности {self.status}'

class Student(Person):
    def __init__(self, name, last_name, university, course):
        super().__init__(name, last_name)
        self.university = university
        self.course = course

    def get_info(self):
        person_info = super().get_info()
        return f'{person_info}, я учусь в {self.university} на {self.course} курсе'
    

person = Person('Иван', 'Петров')
employee = Employee('Иван', 'Петров', 'компании Рога и копыта', 'директор')
student = Student('Иван', 'Петров', 'КГТУ', '3 курсе')

def get_human_info(obj):
    print(obj.get_info())

get_human_info(employee) 
get_human_info(student) 
get_human_info(person)