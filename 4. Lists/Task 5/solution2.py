suitcase = []
items = ['футболка', 'шорты', 'сланцы', 'очки', 'кепка'] 

for item in items:
    suitcase.append(item)

suitcase.pop()
suitcase.insert(0, 'панама')

print(suitcase)