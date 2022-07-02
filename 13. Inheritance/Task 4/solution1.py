class MyDict(dict):
    def get(self, key, default = 'Are you kidding?'):
        return super().get(key, default)

obj_dict = MyDict({'some_title': 2})

print(obj_dict.get('some'))