def forLoopRange():
    for i in range(10):
        print(i)
#forLoopRange()

def forLoopIterable(iterable):
    for val in iterable:
        print(val)
#forLoopIterable('Rey')

def forLoopWithElse(iterable):
    for val in iterable:
        print(val)
        if val == 3:
            break
    else:
        print('no items left')
#forLoopWithElse([1,2,3,4,5])

def whileLoop():
    sum = 0
    start = 1
    end = 10
    while start <= end:
        sum += start
        start += 1
    print('Sum:', sum)
#whileLoop()

def whileLoopWithElse():
    i=0
    sum = 0
    while i <= 5:
        sum += i
        i+=1
    else:
        print('no items left')
    print('Sum:', sum)
#whileLoopWithElse()

# implement search loops
def useCaseForElse(iterable):
    for v in iterable:
        if v == 'python':
            print('{} is COOL'.format(v))
            break
    else:
        print('Cannot find a COOL programming language')
languages = ['visual basic', 'assembly', 'shell', 'php', 'c#', 'python']
useCaseForElse(languages)