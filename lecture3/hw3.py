# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List


def custom_range(inp: List, *args):
    len1 = len(args)
    step = args[2] if len1 > 2 else 1
    stop = args[0] if len1 > 0 else None
    start, stop = (args[0], args[1]) if len1 > 1 else (inp[0], stop)

    if step < 0:
        inp = reversed(inp)
        step = abs(step)

    new_list = []
    write = False
    for i in inp:
        if i == start:
            write = True
        if i == stop:
            return new_list[::step]
        if write:
            new_list.append(i)

    return new_list[::step]
