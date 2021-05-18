import pytest

from homework.homework5.hw2 import *


def test_custom_sum_name_and_doc_check():
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"
    assert custom_sum.__original_func(1, 2, 3, 4, 5) == 15
