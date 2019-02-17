from dog import Dog
from cat import Cat
class AnimalController:
    def __init__(self):
        self.__animals = []
    def addAnimal(self, animal):
        self.__animals.append(animal)
    def makeSounds(self):
        for animal in self.__animals:
            animal.makeSound()
    @property
    def animals(self):
        return self.__animals

if __name__ == '__main__':
    controller = AnimalController()
    controller.addAnimal(Dog('Brownie'))
    controller.addAnimal(Dog('Whitey'))
    controller.addAnimal(Cat('Persey'))
    controller.addAnimal(Cat())
    controller.makeSounds()