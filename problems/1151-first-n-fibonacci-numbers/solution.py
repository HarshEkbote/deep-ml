from functools import reduce
def first_n_fibonacci(n):
    if n==0:
        return []
    fib=lambda n:reduce(lambda x,_:x+[x[-1]+x[-2]],range(n-2),[0,1])
    return fib(n)