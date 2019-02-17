def ifElse(num):
    if num == 0:
        print('{} is zero'.format(num))
    elif num > 0:
        print('{} is a positive number'.format(num))
    else:
        print('{} is a negative number'.format(num))

#ifElse(3)
#ifElse(0)
#ifElse(-3)

def nestedIfElse(num):
    if num >= 0:
        if num == 0:
            print("{} is zero".format(num))
        else:
            print("{} is a positive number".format(num))
    else:
        print("{} is a negative number".format(num))

nestedIfElse(5)
nestedIfElse(0)
nestedIfElse(-5)