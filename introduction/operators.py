x = 2
y = 3
def arithmeticOperators():
    # + - * / % // **
    print('Arithmetic Operators')
    print('x+y:', x + y)
    print("y%x:", y % x)
    print('y**x:', y ** x)
#arithmeticOperators()

def comparisonOperators():
    # > < == != >= <=
    print('Comparison Operators')
    print("x>y", x > y)
    print('x!=y', x != y)
#comparisonOperators()

def bitwiseOperators():
    # & | ~ ^ >> <<
    print('Bitwise Operators')
    print('x&y', x&y)
    print('x|y', x|y)
#bitwiseOperators()

x = True
y = False
def logicalOperators():
    # and or not
    print('Logical Operators')
    print('x and y:',x and y)
    print('x or y:',x or y)
    print('not x:',not x)
#logicalOperators()

def identityOperators():
    # is is not
    print('Identity Operators')
    print('x is True:', x is True)
    print('x is not True:', x is not True)
#identityOperators()

def membershipOperators():
    # in not in
    print('Membership Operators')
    x = 'Python is Cool'
    print('P in x:', 'P' in x)
    print('bad not in x:', 'bad' not in x)
membershipOperators()