"""
利用缓存解斐波那契数例
"""

import sys
from functools import wraps


sys.setrecursionlimit(1000000)  # 解决maximum recursion depth exceeded


def memoization(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memoization
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    result = fib(500)
    print(result)
