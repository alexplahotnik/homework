import itertools
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Finding count of how many tuples (i, j, k, l) there are such
    that A[i] + B[j] + C[k] + D[l] is zero"""
    zero_counter = 0
    for var in itertools.product(a, b, c, d):
        if sum(var) == 0:
            zero_counter += 1
    return zero_counter
