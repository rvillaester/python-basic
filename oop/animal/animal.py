from abc import ABC, abstractmethod
class Animal(ABC):

    def __init__(self, name = 'Animal'):
        self.__name = name

    @abstractmethod
    def makeSound(self):
        pass

    @property
    def name(self):
        return self.__name

if __name__ == '__main__':
    a = Animal()
    a.makeSound()