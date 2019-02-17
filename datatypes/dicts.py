a = {} # empty dictionary
b = {1:'python', 2:'java', 3:'node'} # dictionary with integer keys
c = {'name':'James', 2:[1,0,2]} # dictionary with mixed keys

# create dictionary using the builtin dict()
d = dict({1:'mango', 2:'grapes'})
e = dict([(1,'mango'), (2,'grapes')])

d = {'name':'James', 'age':30, 'address':"Makati"}
# access element from dictionary
#print(d['name'])
#print(d.get("age"))

# change / add / remove elements in dictionary
d["age"]=23
d['mobile']='09187267367'
#print(d)
del d['age']
d.pop("address")
#print(d)

# dictionary comprehension
even_squares = {x: x*x for x in range(1,11) if x%2 == 0}
#print(even_squares)
# dictionary membership
#squares = {x: x*x for x in range(10)}
#print(1 in squares)
#print(11 not in squares)

# iterating a dictionary
def iterateDict():
    squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
    for i, x in squares.items():
        print(i, x)
iterateDict()