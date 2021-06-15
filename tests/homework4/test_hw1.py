import os

import pytest

from homework.homework4.hw1 import read_magic_number


def test_number_from_1to3():
    path = "homework/homework4/test.txt"
    with open(path, "w") as f:
        f.write("2.6\nHello world")
    result = read_magic_number(path)
    os.remove(path)
    assert result


def test_number_not_in_13():
    path = "homework/homework4/test.txt"
    with open(path, "w") as f:
        f.write("14")
    result = read_magic_number(path)
    os.remove(path)
    assert not result


def test_not_number():
    path = "homework/homework4/test.txt"
    with open(path, "w") as f:
        f.write("Im not a number\n2")
    with pytest.raises(ValueError):
        read_magic_number(path)
    os.remove(path)


def test_file_not_exist():
    path = "homework/homework4/test.txt"
    with pytest.raises(ValueError):
        read_magic_number(path)
