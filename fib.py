# -*- coding: utf-8 -*-
def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(list(map(fib, [i for i in range(1, 10)])))
