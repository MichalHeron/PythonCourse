basket = ['a', 'b', 'c', 'd', 'e']


def new_func():
    return 'a' in basket


print(new_func())


# unpacking
a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8]
print(a)
print(b)
print(other)
