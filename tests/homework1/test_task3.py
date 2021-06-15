import pytest

from homework.homework1.task3 import find_maximum_and_minimum


def test_random_input():
    """Test random input"""
    assert find_maximum_and_minimum("tests/homework1/files/test31.txt") == (-7, 444)


def test_sorted_input():
    """Test sorted input"""
    assert find_maximum_and_minimum("tests/homework1/files/test32.txt") == (111, 148)


def test_one_number():
    """Test with only one input"""
    assert find_maximum_and_minimum("tests/homework1/files/test33.txt") == (0, 0)
