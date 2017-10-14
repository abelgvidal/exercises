from itertools import islice

def grouper(n, iterable):
    if not isinstance(n, int) or n < 1:
        raise ValueError("first param should be int and >= 1")
    it = iter(iterable)
    while True:
        chunk = tuple(islice(it, n))
        if not chunk:
            return
        yield chunk
