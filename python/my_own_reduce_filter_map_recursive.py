"""
1. implement you own reduce function
2. implement you own filter and map functions using reduce
"""

def my_reduce(fun, iterable, acum=None):
    for i in iterable:
        acum = fun(acum, i)
    return acum


def my_filter(fun, iterable):
    def ff2(x, y):
        if fun(y):
            x.append(y)
        return x

    return reduce(ff2, iterable, [])


def my_map(fun, iterable):
    def ff2(x, y):
        x.append(fun(y))
        return x

    return reduce(ff2, iterable, [])


def add_cuadrado(acum, y):
    acum.append(y**2)
    return acum


print reduce(add_cuadrado, range(1,10), [])
print my_reduce(add_cuadrado, range(1,10), [])
print map(lambda x: x**2, range(1,10))
print my_map(lambda x: x**2, range(1,10))
print filter(lambda x: x % 2 == 0, range(1,20))
print my_filter(lambda x: x % 2 == 0, range(1,20))

