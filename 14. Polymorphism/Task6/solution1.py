class Language:
    def __init__(self, level, type):
        self.level = level
        self.type = type

class Python(Language):
    def write_function(self, func_name, arg):
        return f'def {func_name}({arg}):'

    def create_variable(self, var_name, value):
        return f'{var_name} = {value.__repr__()}'
        
class JavaScript(Language):
    def write_function(self, func_name, arg):
        a = '{     }'
        return f'function {func_name}({arg}) {a};'

    def create_variable(self, var_name, value):
        return f'let {var_name} = {value.__repr__()};'

py = Python('mid', 3)
print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

js = JavaScript('mid', 4)
print(js.write_function('validate', 'form'))
print(js.create_variable('password', 'john@123'))