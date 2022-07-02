list_ = [1, 1, 3]
answer = 'ERROR'

for num in list_:
    if list_.count(num) > 1:
        answer = 'yes'
        break

print(answer)