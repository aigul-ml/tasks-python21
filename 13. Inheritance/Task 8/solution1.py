class CustomError(Exception):
    def __init__(self, message):
        self.message = message


def check_letters(string):
    if string.isupper():
        return f'ВСЕ ОТЛИЧНО! {string}'
    else:
        raise capitals_error

capitals_error = CustomError("ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ")
print(check_letters("HELLO"))