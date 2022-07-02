class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return f'name:{self.name}, age:{self.age}'

class Student(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty

    def display_student(self):
        person_display = super().display()
        return f'{person_display}, faculty:{self.faculty}'

obj_student = Student('Rick', 21, 'science')
print(obj_student.display())
print(obj_student.display_student())