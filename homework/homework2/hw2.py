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


def major_and_minor_elem(inp: List) -> Tuple[int, set]:
    """Find the most common and the least common elements"""
    elements = set(inp)
    major_elem = inp[0]
    # There can be more, than two minor elements
    minor_elem = set()
    count_least = len(inp)
    for elem in elements:
        if inp.count(elem) > len(inp) // 2:
            major_elem = elem
        if inp.count(elem) < count_least:
            count_least = inp.count(elem)
            minor_elem = {elem}
        elif inp.count(elem) == count_least:
            minor_elem.add(elem)
    return major_elem, minor_elem
