# this is an example of a comment
def statement():
    'This function just shows different kind of statements'
    x = 'single line statement'
    i=1; j=2; team='Super Insurance' # multiple statements in a single line
    a = 1 + 2 + 4 \
        + 5 + 6 + 3 \
        - 7 - 4
    b = (3 + 5
         + 7 + 8
         - 4)
    names = ['rey',
             'niel', 'james',
             'jack']
    print(x,i,j,a,b,names)

statement()
print(statement.__doc__)