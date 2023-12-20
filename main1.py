class Iterator():
    def __init__(self, max_num):
        self.i = -2
        self.max_num = max_num
    def __iter__(self):
        self.i = -2
        return self
    def __next__(self):
        def gen():
            i=0
            while i!= 10:
                yield i
        generator = gen()
        if self.i > self.max_num:
            raise StopIteration
        return generator
iterator = Iterator(10)
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
