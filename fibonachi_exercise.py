class GenFib:
    """Class for generating Fibonacci sequence"""

    def __init__(self, index):
        self.index = index

    def __iter__(self):
        self.a = 0
        self.b = 1
        self.currentIndex = 0
        return self

    def __next__(self):
        fib = self.a
        if self.currentIndex > self.index:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.currentIndex += 1
        return fib


def gen_fib(index):
    if index == 0:
        yield 0
    a = 0
    b = 1
    for number in range(index):
        a, b = b, a + b
        yield a


g2 = GenFib(0)
for i in g2:
    print(i)

g = gen_fib(0)
for i in g:
    print(i)
