num = int(input())

if (num in range(ord('A'), ord('Z') + 1) or 
    num in range(ord('a'), ord('z') + 1)):
    print(f'Это буква "{chr(num)}"')
else:
    print(f'Это не буква, а символ "{chr(num)}"')