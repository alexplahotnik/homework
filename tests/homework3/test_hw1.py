import pytest

from homework.homework3.hw1 import decorator_cache_maker


def test_decorator_works_x_times():
    counter = 0

    @decorator_cache_maker(times=2)
    def test_funktion(a, b, **kwargs):
        nonlocal counter
        counter += 1
        return a + b + sum(kwargs.values())

    test_funktion(1, 2)
    assert counter == 1
    test_funktion(1, 2)
    assert counter == 1
    test_funktion(1, 2)
    assert counter == 1
    test_funktion(1, 2)
    assert counter == 2


def test_decorator_separatly_arguments():
    counter = 0

    @decorator_cache_maker(times=1)
    def test_funktion(a, b, **kwargs):
        nonlocal counter
        counter += 1
        return a + b + sum(kwargs.values())

    test_funktion(1, 2, key=4)
    assert counter == 1
    test_funktion(2, 3)
    assert counter == 2
    test_funktion(1, 2, key=4)
    assert counter == 2
    test_funktion(1, 2, key=4)
    assert counter == 3
