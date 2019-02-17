def times2(n):
    "This returns number multiply by 2"
    return n * 2
#print(times2(2))
#print(times2.__doc__)

def voidFunction():
    print('no void function in python')
    print('if no explicit return then it will return None')
    return
#v = voidFunction();
#print(v)

def withDefaultParamValue(name, msg = 'How are you'):
    print('Hi {0}, {1}'.format(name, msg))
    return
#withDefaultParamValue("Rey")
#withDefaultParamValue("Rhoda", 'Good Morning')
#withDefaultParamValue(msg = 'Good day', name = "Jason")

def withArbitraryArgs(*numbers):
    sum = 0
    for n in numbers:
        sum += n;
    print('Sum', sum)
    return
withArbitraryArgs(2,45,6,7)
withArbitraryArgs(-5,0,9,-45)