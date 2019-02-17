def implicit():
    a = 1
    b = 2.3
    c = a + b
    print(c, type(c))
#implicit()

def implicit1():
    a = 1
    b = '2'
    print(type(a), type(b))
    c = a + b
    print(c, type(c))
#implicit1()

def explicit():
    a = 1
    b = '2'
    c = a + int(b)
    print(c, type(c))
explicit()