a = set() # empty set
b = {1, 2, 3} # list of integers
c = {1, "Hello", 'python', 3.4} # list of mixed types

numbers = {1, 2, 3, 5}
# change set elements
#numbers.add(4)
#numbers.update([6,7,2,1])
#numbers.discard(4)
#numbers.remove(2)
#numbers.pop()

x = {1,2,3,4,5}
y = {4, 5, 6, 7, 8}
#set operations
#print(x.union(y))
#print(x.intersection(y))
#print(x.difference(y))
#print(x.symmetric_difference(y))

def membership(l):
    if l in x:
        print('{} is a member in the list'.format(l))
    else:
        print('{} is not a member in the list'.format(l))
#membership('java')

def iterate():
    for l in x:
        print(l)
#iterate()

def commonMethods():
    print(len(x))
    print(min(x))
#commonMethods()