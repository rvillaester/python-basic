class EvenOnly:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.counter = 2
        return self
    def __next__(self):
        if self.counter <= self.max:
            value = self.counter
            self.counter += 2
            return value
        else:
            raise StopIteration

for i in EvenOnly(10):
    print(i)

#print(dir(list))
print(dir(int))