class Class1:
    def first(self):
        pass

    def second(self):
        pass

class Class2(Class1):
    def third(self):
        pass
    
    def fourth(self):
        pass

obj = Class2()
obj.first()
obj.second()
obj.third()
obj.fourth()