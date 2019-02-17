class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    def __str__(self):
        return 'x:{}, y:{}'.format(self.x, self.y)

x = 3
print(type(x), x)
print(dir(x))
y = 2
z = x + y
#print(type(z), z)
#print(dir(int))

a = Point(2, 3)
b = Point(4, 5)
c = a + b
print('g', c)
