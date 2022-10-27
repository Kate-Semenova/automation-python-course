"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from copy import copy
from typing import Any, List

one_combination = []
test_list = []
start = True
length: int


def combinations(*args: List[Any]) -> List[List]:
    global start
    global length

    local_list = []
    if start:
        length = len(args)
        start = False
    for i in range(len(args)):
        for i_n in range(len(args[i])):
            one_combination.append(args[i][i_n])
            combinations(*args[i + 1:])
            if len(one_combination) == length:
                test_list.append(copy(one_combination))
            one_combination.remove(args[i][i_n])
        if i == length - 1:
            local_list = copy(test_list)
            test_list.clear()
            start = True
    return local_list
