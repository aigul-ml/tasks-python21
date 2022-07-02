def add(num1, num2):
    result = sum((num1, num2))
    return result

# Способ через встроенную функцию sum(но int не итерируемый объект и  
# из-за этого мы ооборачиваем его tuple)