class A:
    @staticmethod # staticmethod - это декоратор который превращает наш метод в статический метод.
    def method1(self): # Cтатический метод - это обычная функция объявленная внутри класса.
        print('Hello World')

class B(A):
    pass

b1 = B()

b1.method1()