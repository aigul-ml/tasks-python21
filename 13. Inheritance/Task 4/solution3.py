class MyDict(dict):
    def get(self, key, default = 'Are you kidding?'):
        try:
            value = self[key]
        except KeyError:
            return default
        return value

obj_dict = MyDict({'some_title': 2})

print(obj_dict.get('some'))