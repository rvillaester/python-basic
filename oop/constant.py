class ConstantException(TypeError):
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return "Can't rebind constant: {}".format(self.message)

class Constant:
    def __setattr__(self, key, value):
        if key in self.__dict__:
            raise ConstantException(key)
        self.__dict__[key] = value

import sys
sys.modules[__name__]=Constant()

if __name__ == '__main__':
    import constant
    constant.a = 1
    print(constant.a)
    #constant.a = 2
    print(constant.a)