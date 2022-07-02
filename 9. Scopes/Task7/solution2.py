a = ['pipi', 'papa', 'mama']
b = list()

def title_in_list():
    global a
    global b
    for string in a:
        string = string.title()
        b.append(string)
    print(b)
    
title_in_list()

