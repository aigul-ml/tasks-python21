class A:
    def method1(self):
        print('Основной функционал')

class B(A):
    def method1(self):
        A.method1(self)
        print('Дополнительный функционал')

obj = B()
obj.method1()