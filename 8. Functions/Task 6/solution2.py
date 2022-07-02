num = 6

def check(num):
    even_odd = 'even' if not num % 2 else 'odd'
    return f'It is {even_odd} number'

print(check(num))