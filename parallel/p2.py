import multiprocessing as mp


def cube(x):
    return x**3

pool = mp.Pool(processes=4)


# results = [pool.apply(cube, args=(x,)) for x in range(1,7)]
# print(results)


# results = pool.map(cube, range(1,7))
# print(results)


results = [pool.apply_async(cube, args=(x,)) for x in range(1,7)]
output = [p.get() for p in results]
print(output)
