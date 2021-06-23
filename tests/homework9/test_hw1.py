import pytest

from homework.homework9.hw1 import merge_sorted_files


def test_three_files():
    files = [
        "tests/homework9/examples/test_1.txt",
        "tests/homework9/examples/test_2.txt",
        "tests/homework9/examples/test_3.txt",
    ]
    result = merge_sorted_files(files)
    assert list(result) == [1, 3, 4, 6, 7, 8, 13, 15, 19, 21, 99]
    with pytest.raises(StopIteration):
        next(result)
