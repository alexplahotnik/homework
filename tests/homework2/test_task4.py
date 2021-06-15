import pytest

from homework.homework2.hw4 import cache


def test_cash_func():
    """Testing function"""

    def func(a, b, c):
        return a + b + c

    some = "ac", "dc", "rule"
    val_1 = cache(func)(*some)
    val_2 = cache(func)(*some)
    assert val_1 == val_2
