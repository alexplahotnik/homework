import pytest

from homework.homework2.hw2 import major_and_minor_elem


def test_regular_input():
    """Testing regular inputs"""
    assert major_and_minor_elem([1, 8, 1, 1, 8, 1, 2]) == (1, {2})


def test_one_input():
    """Testing list with only one number"""
    assert major_and_minor_elem([2]) == (2, {2})


def test_two_minor():
    """Testing list with two minor numbers"""
    assert major_and_minor_elem([7, 7, -3, 7, -3, 7, 4, 4, 7]) == (7, {-3, 4})
