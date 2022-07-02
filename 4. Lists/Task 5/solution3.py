suitcase = []
items = ['футболка', 'шорты', 'сланцы', 'очки', 'кепка'] 
i = 0

while i < len(items):
    suitcase.append(items[i])
    i += 1

suitcase.remove(suitcase[-1])
suitcase.insert(0, 'панама')

print(suitcase)