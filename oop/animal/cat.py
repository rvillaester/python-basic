from animal import Animal
class Cat(Animal):

    def __init__(self, name = 'Cat'):
        super().__init__(name)

    def makeSound(self):
        print('My name is {} and I say Meowwwww'.format(self.name))

if __name__ == '__main__':
    a = Cat('Kitty')
    a.makeSound()
    #print(dir(a))