"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable

cash = {}


def cache(func: Callable) -> Callable:
    def cache_func(*args):
        if cash.get(func) is None:
            cash.setdefault(func, {args: func.__call__(*args)})
        if cash.get(func).get(args) is None:
            cash.get(func).setdefault(args, func.__call__(*args))
        return cash.get(func).get(args)

    return cache_func


def cache_with_local(func: Callable) -> Callable:
    cash_local = {}

    def cache_func(*args):
        print(args)

        if cash_local.get(args) is None:
            cash_local.setdefault(args, func.__call__(*args))
        return cash_local.get(args)

    return cache_func
