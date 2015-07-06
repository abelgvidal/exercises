import multiprocessing as mp
from random import randint
from time import sleep


def wait_rand(pos):
    random_num = randint(0,5)
    sleep(random_num)
    print pos, random_num, "*** print as-you-go ***"
    return pos, random_num

pool = mp.Pool(processes=4)
results = [pool.apply_async(wait_rand, args=(x,)) for x in range(1,7)]
output = [p.get() for p in results]

print "final results"
print output
