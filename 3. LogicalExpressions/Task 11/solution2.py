import string

num = int(input())

if chr(num) in string.ascii_letters:
    print(f'Это буква "{chr(num)}"')
else:
    print(f'Это не буква, а символ "{chr(num)}"')