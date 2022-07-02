class CreateMixin:
    def create(self, key, todo):
        if key in self.todos.keys():
            return 'Задача под таким ключём уже существует'
        self.todos[key] = todo
        return self.todos

class DeleteMixin:
    def delete(self, key):
        res = None
        if key in self.todos.keys():
            res = self.todos.pop(key)
        return res

class UpdateMixin:
    def update(self, key, new_value):
        self.todos.update({key:new_value})
        return self.todos

class ReadMixin:
    def read(self):
        res = [x for x in self.todos.items()]
        return sorted(res)

class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    def __init__(self):
        self.todos = {}

    def set_deadline(self, data):
        from datetime import date
        data = data.split('/')
        dead_line = date(int(data[2]), int(data[1]),int(data[0]))
        date_now = date.today()
        res = dead_line - date_now
        return res.days

task = ToDo()

print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2,'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('6/7/2022'))