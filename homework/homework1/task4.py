from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    """Finding count of how many tuples (i, j, k, l) there are such 
    that A[i] + B[j] + C[k] + D[l] is zero"""
    zero_summ = 0
    for i in a:
        for j in b:
            for k in c:
                for l in d:
                    if i + j + k + l == 0:
                        zero_summ += 1
    return zero_summ
