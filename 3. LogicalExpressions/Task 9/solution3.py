year = int(input())

result = (
    'YES' if year % 4 == 0 and 
    year % 100 != 0 or 
    year % 400 == 0 else 'NO'
)

print(result)