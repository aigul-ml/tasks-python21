class A:
    @classmethod # classmethod - это декоратор который превращает наш метод в метод класса.
    def method1(cls): # Метод класса - это метод который первым аргументом принимает сам класс.
        print('Hello World')

class B(A):
    pass

b1 = B()

b1.method1()