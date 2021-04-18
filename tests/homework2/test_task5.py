import string

import pytest

from homework.homework2.hw5 import custom_range


def test_one_value():
    """Testing with one argument"""
    assert custom_range(string.ascii_lowercase, "e") == ["a", "b", "c", "d"]


def test_two_values():
    """Testing with two argument"""
    assert custom_range(string.ascii_lowercase, "c", "i") == [
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
    ]


def test_step():
    """Testing with step"""
    assert custom_range(string.ascii_lowercase, "c", "i", 2) == ["c", "e", "g"]


def test_error():
    """Testing error case"""
    assert custom_range(string.ascii_lowercase, "в") == "Wrong values"
