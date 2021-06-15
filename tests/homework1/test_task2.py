import pytest

from homework.homework1.task2 import check_fibonacci


def test_real_fibonacci_sequence():
    """Testing positive result"""
    assert check_fibonacci([1, 1, 2, 3, 5, 8, 13])


def test_fake_sequence():
    """Testing false result"""
    assert not check_fibonacci([1, 1, 2, 3, 7, 4, 11])


def test_not_enough_data():
    """Testing 2 or less numbers"""
    with pytest.raises(ValueError):
        check_fibonacci([2, 3])
