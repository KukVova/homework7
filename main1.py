class Iterator():
    def __init__(self, max_num):
        self.i = 0
        self.max_num = max_num
    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i == self.max_num:
            raise StopIteration
        def gen():
            n = 0
            while n != 10:
                n += 2
                yield n

        return gen

i = Iterator(5)

g = i.__next__()
f = g()
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

