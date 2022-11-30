# 1. Implement a function that flatten incoming data:
# non-iterables and elements from iterables (any nesting depth should be supported)
# function should return an iterator (generator function)
# don't use third-party libraries

def merge_elems(*elems):
    for _ in elems:
        if not hasattr(_, '__iter__') or (type(_) is str and len(_) == 1):
            yield _
        else:
            for e1 in _:
                yield from merge_elems(e1)


for i in merge_elems([[[[[[[1, "sdfghjk", [2, 1.2, [3, 4]]]]]]]]], 5, "dfwe", 'd', [1, 2, 3], {"a": 1, "b": 2}, 4,
                     [[1, 2], [3, 4]], ):
    print(i, end=' ')
a = [1, 2, 3]
b = 6
c = 'zhaba'
d = [[1, 2], [3, 4]]
print()

for _ in merge_elems(a, b, c, d):
    print(_, end=' ')
    # output: 1 2 3 6 z h a b a 1 2 3 4


# 2. Implement a map-like function that returns an iterator (generator function)
# extra functionality: if arg function can't be applied, return element as is + text exception

def map_like(fun, *elems):
    for _ in elems:
        try:
            yield fun(_)
        except Exception as e:
            yield f"{_}: {e}"


a = [1, 2, 3]
b = 6
c = 'zhaba'
d = True
fun_e = lambda x: x[0]
fun_test = lambda x: str(x)
print()
for _ in map_like(fun_e, a, b, c, d):
    print(_)
    # output:
    # 1
    # 6: 'int' object is not subscriptable
    # z
    # True: 'bool' object is not subscriptable
