"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    major: str
    minor: str
    my_dictionary = {}
    for each in inp:
        my_dictionary.setdefault(each, inp.count(each))
    return max(my_dictionary, key=my_dictionary.get), min(my_dictionary, key=my_dictionary.get)


def major_and_minor_elem_2(inp: List) -> Tuple[int, int]:
    my_dictionary = {}
    a = 0
    b = len(inp)
    least_amount = len(inp) // 2
    major: str
    minor: str
    for i in inp:
        count = my_dictionary.get(i)
        if count is None:
            my_dictionary.setdefault(i, 1)
        else:
            my_dictionary.update([(i, count + 1)])
    for key, item in my_dictionary.items():
        if item > a and item >= least_amount:
            a = item
            major = key
        if item < b:
            b = item
            minor = key
    return major, minor


def major_and_minor_elem_2(inp: List) -> Tuple[int, int]:
    new_set = set(inp)
    print(new_set)
    a = 0
    b = len(inp)
    least_amount = len(inp) // 2
    major: str
    minor: str
    for i in new_set:
        count = inp.count(i)
        if a < count and count >= least_amount:
            a = count
            major = i
        if b > count:
            b = count
            minor = i
    return major, minor
