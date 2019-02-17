def numberType():
    a = 5 # int
    print(type(a))
    b = 5.0 # float
    print(type(b))
    c = 5 + 3j # complex
    print(c, type(c))
#numberType()

def numberSystem():
    a = 0b1101011
    print('binary:', a)
    b = 0o15
    print('octal:', b)
    c = 0xFB
    print('hexadecimal', c)
numberSystem()