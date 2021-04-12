import pytest
from homework.homework1.task4 import check_sum_of_four


def test_core_function():
    """Test of function"""
    assert check_sum_of_four([1, 6], [5, 3], [-3, -6], [0, -3]) == 3


def test_empty_lists():
    """Testing with empty lists"""
    assert check_sum_of_four([], [], [], []) == 0
