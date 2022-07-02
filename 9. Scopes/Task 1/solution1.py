def foo():
    global var
    var = 'переменная foo'

    def bar():
        global var
        print(f'переменная в foo:  {var}')
        var = 'переменная bar'

    bar()
foo()
print("переменная в foo: ", var)