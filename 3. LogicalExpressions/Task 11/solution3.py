num = int(input())

if chr(num).isalpha():
    print(f'Это буква "{chr(num)}"')
else:
    print(f'Это не буква, а символ "{chr(num)}"')