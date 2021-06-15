import pytest

from homework.homework1.task5 import find_maximal_subarray_sum


def test_k_elements():
    """If max sum need k numbers in sub-array"""
    assert find_maximal_subarray_sum([2, -3, 5, 6, 1], 3) == 12


def test_zero_elements():
    """If empty list have a biggest sum"""
    assert find_maximal_subarray_sum([-1, -3, -4, -2, -7], 2) == 0


def test_middle_elements():
    """If max summ need less that k numbers in sub-array"""
    assert find_maximal_subarray_sum([5, 2, -6, -1, 2, 11, -4, 5], 3) == 13


def test_empty_list():
    """If list is empty"""
    with pytest.raises(ValueError):
        find_maximal_subarray_sum([], 7)
