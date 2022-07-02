from abc import ABC, abstractmethod

class Coder(ABC):
    count_code_time = 0

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def coding(self):
        pass

class Backend(Coder):
    def __init__(self, experience, languages_backend):
        self.languages_backend = languages_backend
        self.experience = experience
        
    def get_info(self):
        return f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

    def coding(self, count):
        self.count_code_time += count

class  Frontend(Coder):
    def __init__(self, experience, languages_frontend, ):
        self.languages_frontend = languages_frontend
        self.experience = experience
        
    def get_info(self):
        return f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование'

    def coding(self, count):
        self.count_code_time += count

class Fullstack(Frontend, Backend):
    pass

a = Backend('Senior', 'Ruby')
b = Frontend('Junior', 'C++')
c = Fullstack('Middle', 'HTML')
a.coding(100)
b.coding(520)
c.coding(298)
print(a.get_info())
print(b.get_info())
print(c.get_info())