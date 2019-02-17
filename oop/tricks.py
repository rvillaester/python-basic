class ObjectTricks:
    'This is the doc string for this class'
    classAttr1 = 1
    classAttr2 = 'Class attribute'
    __privateClassAttr = 'Private class attribute'

    def __init__(self, param = 'Default Value'):
        self.instanceAttr1 = 'Python'
        self.instanceAttr2 = ObjectTricks.classAttr1 + 1
        self.instanceAttr3 = [x for x in range(5)]
        self.__instanceAttr4 = param
    def trick1(self):
        print(ObjectTricks.__privateClassAttr)
        print(self.__privateClassAttr)
    def trick2(self):
        print(self.__instanceAttr4)
    def __privateMethod(self):
        print('this method is private and of course it can access class and instance properties')
        print(self.__privateClassAttr)
        print(self.__instanceAttr4)
    @classmethod
    def classMethod(cls):
        print('this is a class method')
        print(cls.classAttr1)
    @staticmethod
    def staticMethod():
        print('this is a static method')
        print(ObjectTricks.classAttr1)

# ----------------------------------------

def classAttribTricks():
    ot = ObjectTricks()
    print(ot.__doc__)
    print(ObjectTricks.classAttr1)
    print(ot.classAttr2)
    #print(ObjectTricks.__privateClassAttr)
    ot.trick1()
    print(dir(ot))
    print(ot._ObjectTricks__privateClassAttr)
#classAttribTricks()

def instanceAttribTricks():
    ot = ObjectTricks('user param')
    print(ot.instanceAttr1)
    print(ot.instanceAttr2)
    print(ot.instanceAttr3)
    #print(ot.__instanceAttr4)
    ot.trick2()
    print(dir(ot))
    print(ot._ObjectTricks__instanceAttr4)
    ot._ObjectTricks__instanceAttr4 = 'new param'
    print(ot._ObjectTricks__instanceAttr4)
#instanceAttribTricks()

def privateMethodTricks():
    ot = ObjectTricks()
    print(dir(ot))
    #ot.__privateMethod()
    ot._ObjectTricks__privateMethod()
#privateMethodTricks()

ObjectTricks.staticMethod()
ot = ObjectTricks()
ot.classMethod()
