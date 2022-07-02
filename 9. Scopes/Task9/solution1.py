a = list()

def append_to_list():
    global a
    for num in range(11):
        a.append(num)
    print(a)
    
append_to_list()