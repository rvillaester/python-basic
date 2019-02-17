from animal import Animal
class Dog(Animal):

    def __init__(self, name = 'Dog'):
        super().__init__(name)

    def makeSound(self):
        print('My name is {} and I say Awwwwwwww'.format(self.name))

if __name__ == '__main__':
    a = Dog()
    a.makeSound()