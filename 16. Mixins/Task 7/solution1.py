class ExtensionMixin:
    def add_extension(self, extension):
        self.extensions.append(extension)
        return f'Добавлено новое расширение {extension} для игры {self.name}'
    
    def remove_extension(self, extension):
        if extension in self.extensions:
            self.extensions.remove(extension)
            return f'{extension} был отключен от {self.name}'
        return 'Такого расширения нет в списке.'

class Game(ExtensionMixin):
    def __init__(self, name, type):
        self.type = type
        self.name = name
        self.extensions = []

    def get_description(self, desc):
        return f'{self.name} это {desc}'

    def get_extensions(self):
        if not self.extensions:
            return 'Нет подключенных расширений'
        return self.extensions

game = Game(10, 'Minecraft')

print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром.'))
print(game.add_extension('Multiverse-Core'))
print(game.get_extensions())