def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibi(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]

from timeit import Timer
from fibo import fib

t1 = Timer("fib(10)","from fibo import fib")

for i in range(1,41):
    s = "fib(" + str(i) + ")"
    t1 = Timer(s,"from fibo import fib")
    time1 = t1.timeit(3)
    s = "fibi(" + str(i) + ")"
    t2 = Timer(s,"from fibo import fibi")
    time2 = t2.timeit(3)
    s = "fibm(" + str(i) + ")"
    t3 = Timer(s,"from fibo import fibm")
    time3 = t3.timeit(3)

    print("n=%2d, fib: %8.6f, fibi:  %7.6f, fibm: %8.6f, percent: %10.2f" % (i, time1, time2, time3, time1/time2))
