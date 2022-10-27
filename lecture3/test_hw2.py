from hw2 import cache, cache_with_local


def test_cache():
    def func(a, b):
        return (a ** b) ** 2

    def func_2(q, w):
        return q * q

    cache_func = cache_with_local(func)
    cache_func_2 = cache_with_local(func_2)

    some = 100, 200

    val_1 = cache_func(*some)
    val_2 = cache_func(*some)
    val_3 = cache_func(2, 2)
    val_4 = cache_func(2, 2)

    val_5 = cache_func(*some)
    val_6 = cache_func_2(*some)

    assert val_1 is val_2
    assert val_3 is val_4
    assert val_5 is not val_6
