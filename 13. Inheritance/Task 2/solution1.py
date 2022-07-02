class A:
    def method1(self):
        print('Основной функционал')

class B(A):
    def method1(self):
        super().method1() # super() позволяет на вызвать метод родительского класса
        print('Дополнительный функционал')

obj = B()
obj.method1()