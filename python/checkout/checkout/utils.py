"""here some utilities"""
from itertools import islice

def grouper(n, iterable):
    """group an iterable in a list for iterables of n size"""
    if not isinstance(n, int) or n < 1:
        raise ValueError("first param should be int and >= 1")
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk
