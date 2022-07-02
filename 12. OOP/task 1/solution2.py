class Song:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def show_author(self):
        return 'Автор этой песни ' + self.author

    def show_title(self):
        return 'Название этой песни ' + self.title

    def show_year(self):
        return 'Эта песня вышла в ' + str(self.year) + ' году'

song = Song('Happy', 'Pharrell Williams', 2013)
print(song.show_title())
print(song.show_author())
print(song.show_year())