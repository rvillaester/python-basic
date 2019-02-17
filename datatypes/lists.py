a = [] # empty list
b = [1, 2, 3] # list of integers
c = [1, "Hello", 3.4] # list of mixed types
c = ['python', [2,0,1], 5] # nested list

numbers = [1,2,4,5]
def addElement():
    numbers.append(6)
    print(numbers)
    numbers.insert(2, 3)
    print(numbers)
#addElement()

def removeElement():
    numbers.remove(4)
    print(numbers)
    del numbers[0]
    print(numbers)
#removeElement()

lst = [1, 'java', 5.6, 'python', [2,3]]
def accessElement():
    print(lst[2])
    print(lst[-2])
    print(lst[-1][0])
#accessElement()

def slicing():
    print(lst[1:3])
    print(lst[:3])
    print(lst[2:])
    print(lst[-3:])
#slicing()

def membership(l):
    if l in lst:
        print('{} is a member in the list'.format(l))
    else:
        print('{} is not a member in the list'.format(l))
#membership('java')

def iterate():
    for l in lst:
        print(l)
#iterate()

def commonMethods():
    print(len(lst))
    print(lst.index('python'))
#commonMethods()

#list comprehension
def listComprehension(n):
    evenNumbers = [v for v in range(1, n) if v%2==0]
    print('Even numbers:', evenNumbers)
    numberSquare = [v * v for v in range(n)]
    print('Number square:', numberSquare)
listComprehension(10)