def times3(x):
    return x * 3
#print(times3(3))

t3 = lambda x: x * 3
#print(t3(3))

def filterEvenNumbers(numbers):
    evenLambda = lambda x: x%2==0
    return list(filter(evenLambda, numbers))

numbers = [1,3,4,7,8]
#even = filterEvenNumbers(numbers)
#print(even)

times2 = list(map(lambda x: x * 2 , numbers))
print(times2)