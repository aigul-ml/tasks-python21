class CreateMixin:
    def create(self, key, todo):
        res = self.todos.get(key)
        if res:
            return 'Задача под таким ключём уже существует'
        else:
            self.todos.update({key: todo})
        return self.todos

class DeleteMixin:
    def delete(self, key):
        res = None
        if key in self.todos.keys():
            res = self.todos[key]
            del self.todos[key]
        return res

class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos

class ReadMixin:
    def read(self):
        res = [x for x in self.todos.items()]
        res.sort()
        return res

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}

    def set_deadline(self, data):
        from datetime import date
        data = reversed(data.split('/'))
        data = list(map(int, data))
        dead_line = date(*data)
        res = dead_line - date.today()
        return res.days

task = ToDo()

print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2,'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('6/7/2022'))