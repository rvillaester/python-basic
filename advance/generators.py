def evenOnlyGenerator(max):
    counter = 2
    while counter <= max:
        yield counter
        counter += 2

#for i in evenOnlyGenerator(10):
    #print(i)

def generatorComprehension():
    even = (i for i in range(1,20) if i%2==0)
    print(type(even))
    for e in even:
        print(e)

generatorComprehension()