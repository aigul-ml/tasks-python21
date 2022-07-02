class MyDict(dict):
    def get(self, key, default = 'Are you kidding?'):
        return dict.get(self, key, default)

obj_dict = MyDict({'some_title': 2})

print(obj_dict.get('some'))