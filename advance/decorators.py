# format
def decorator(func):
    def inner():
        # do things before function call
        func()
        # do things after function call
    return inner

def normal():
    pass

decorated = decorator(normal)










# example
def make_fancy(func):
    def inner():
        print('I am happy')
        func()
        print('I am lively')
    return inner

def boring(msg = 'I am boring'):
    print(msg)

#boring()
#decorated = make_fancy(boring)
#decorated()









# using annotation
@make_fancy
def lonely(msg = 'I am lonely'):
    print(msg)

#lonely()





# sample use cases

# calculating runtime
import time
def calculateRuntime(func):
    def calculate(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        elapsedTime = endTime - startTime
        print('Runtime for {} is {}'.format(func.__name__, elapsedTime))
    return calculate

@calculateRuntime
def longRunningFunction():
    print('Pretend that this function is doing a lot of things and we wanted to know the runtime')
    time.sleep(1)

#longRunningFunction()










# check for null params
def checkNoneParam(func):
    def check(*args, **kwargs):
        params = list(args)
        params.extend(list(kwargs.values()))
        if params:
            for p in params:
                if not p:
                    print('Cannot accepts None parameter')
                    break
                    #raise ValueError('Null')
            else:
                func(*args, **kwargs)
    return check

@checkNoneParam
def sampleMethod(*args, **kwargs):
    print('This method only executes when no params are None')

sampleMethod('rey', name = None)