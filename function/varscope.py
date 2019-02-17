a = 'global'

def func():
    global a
    a = 'g'
    b = 'local'
    print(a, b)
    def inner():
        nonlocal b
        c = 'inner'
        b = 'l'
        print(a, b, c)
    inner()
    print(b)

func()
print(a)