def count_symbols(str_):
    vowels = 0
    consonants = 0
    symbols = 0
    
    for l in str_.lower():
        if l in "йуеыаоэяиюё":
            vowels += 1 
        elif l in "цкнгшщзмчвфжрлдтсп":
            consonants += 1
        else:
            symbols += 1
    return f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов: {symbols}'

print(count_symbols('Мурат супер'))