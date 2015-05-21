

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res


def nint(n, total=0):
    if n == 0: return total
    return  n + nint(n-1, total)


def printt(a, b):
    print a,b

[(printt(a, factorial(a))) for a in [5]]


[(printt(a, nint(a))) for a in range(1,100)]



