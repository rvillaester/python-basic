from math import pi as p

def imp():
    print(p)
#imp()
#print(p.__doc__)

def formatting():
    print('this will be printed on the screen')
    name = 'Python'
    age=21
    print('print name on the screen:', name, age)
    print(1,2,3,4, sep=':ython')

    x=1;y=2
    print('x is {} and y is {}'.format(x, y))

    bread='bread'
    butter='butter'
    print('I love {1} and {0}'.format(bread, butter))
    print('I love {x} and {y}'.format(x = bread, y = butter))
formatting()