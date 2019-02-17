a = 'hi'
b = "Hello"
c = '''Good day'''
c = """Welcome to
    Python Programming
    Language"""

str = 'Python is Cool'
def accessElement():
    print(str[2])
    print(str[-1])
#accessElement()

def slicing():
    print(str[1:3])
    print(str[:3])
    print(str[6:])
    print(str[-3:])
#slicing()

def concatenation():
    x = 'Python '
    y = 'is Cool'
    print(x + y)
#concatenation()

def membership(s):
    if s in str:
        print('Member')
    else:
        print('Not a member')
#membership('o')

def iterate():
    for s in str:
        print(s)
#iterate()

def commonMethods():
    s = 'pyThOn'
    print(s.lower())
    print(s.upper())
commonMethods()