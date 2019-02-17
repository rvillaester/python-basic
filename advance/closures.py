def outer(a):
    def inner(b):
        return 'outer a is {}, inner b is {}'.format(a, b)
    return inner

o = outer('Python')
#print(o('Java'))


def multiplyValueOfList(l):
    def copy(n):
        return [i*n for i in l]
    return copy

numbers = [i for i in range(1,5)]
print(numbers)
multiplier = multiplyValueOfList(numbers)
print(multiplier(3))