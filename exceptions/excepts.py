def division(a, b):
    try:
        c = a/b
    except ZeroDivisionError:
        print('Opps zero')
    except TypeError:
        print('Type Error')
    else:
        print('continue')
        return c

#quotient = division(2,'i0')
#print(quotient)
#division(2,0)

def doubleEvenNumber(l):
    for i, v in enumerate(l):
        try:
            x = int(v)
        except ValueError:
            print('Oppps {} is not a number'.format(v))
        else:
            l[i] = x*2 if x%2==0 else x

lst = [1,2,'3f',4]
#doubleEvenNumber(lst)
#print(lst)

def openAndCloseFile(filename):
    try:
        f = open(filename, 'w')
        f.write('line to be written')
    finally:
        f.close()

openAndCloseFile('t.txt')