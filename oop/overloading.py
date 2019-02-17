class Person:
    def __init__(self, name, address = None):
        self.name = name
        self.address = address
    def makeGreetingsTo(self, personToGreet, message = 'Good Morning'):
        print('{} say: Hi {}, {}'.format(self.name, personToGreet.name, message))
    def unknownNumberOfArgs(self, *args, **kwargs):
        print(args)
        print(kwargs)
    def __str__(self):
        str = 'I am {} and my address is {}'
        if self.address is None:
            address = 'Not specified'
        else:
            address = self.address
        return str.format(self.name, address)

def constructorOverloading():
    rey = Person('Rey')
    print(rey)
    albert = Person('Albert', 'Makati')
    print(albert)
#constructorOverloading()

def methodOverloading():
    rey = Person('Rey')
    albert = Person('Albert')
    rey.makeGreetingsTo(albert)
    albert.makeGreetingsTo(rey, 'How are you')
#methodOverloading()

def multipleParams():
    rey = Person('Rey')
    #rey.unknownNumberOfArgs(2, 'James', 6.7, age = 8, gender = 'Male')
    rey.unknownNumberOfArgs()
multipleParams()