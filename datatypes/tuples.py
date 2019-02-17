a = () # empty tuple
b = (1, 2, 3) # tuple of integers
c = (1, "Hello", 3.4) # tuple of mixed types
c = ('python', [2,0,1], 5, ('a', 'b', 'c')) # nested tuple

tup = (1, 'java', 5.6, 'python', [2,3])
def accessElement():
    print(tup[2])
    print(tup[-2])
    print(tup[-1][0])
#accessElement()

def slicing():
    print(tup[1:3])
    print(tup[:3])
    print(tup[2:])
    print(tup[-3:])
#slicing()

def membership(l):
    if l in tup:
        print('{} is a member in the list'.format(l))
    else:
        print('{} is not a member in the list'.format(l))
#membership('java')

def iterate():
    for l in tup:
        print(l)
#iterate()

def commonMethods():
    print(len(tup))
    print(tup.index('python'))
#commonMethods()