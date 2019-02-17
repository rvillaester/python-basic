class Person:
    def __init__(self, age=0):
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

p = Person(12)
print(p.age)
p.age = 10
print(p.age)
