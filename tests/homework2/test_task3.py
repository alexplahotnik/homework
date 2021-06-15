import pytest

from homework.homework2.hw3 import combinations


def test_regular_case():
    """Testing, that function is really work"""
    assert combinations([1, 2], [2, 3], [4, 5]) == [
        [1, 2, 4],
        [1, 2, 5],
        [1, 3, 4],
        [1, 3, 5],
        [2, 2, 4],
        [2, 2, 5],
        [2, 3, 4],
        [2, 3, 5],
    ]


def test_diff_size():
    """Testing with different-sized input lists"""
    assert combinations([1, 2], [5, 7, 8]) == [
        [1, 5],
        [1, 7],
        [1, 8],
        [2, 5],
        [2, 7],
        [2, 8],
    ]
