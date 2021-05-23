import pytest

from homework.homework8.hw1 import KeyValueStorage


def test_attr_stored():
    some_obj = KeyValueStorage("homework/homework8/task1_example.txt")
    assert some_obj.name == "kek"
    assert some_obj.power == 9001


def test_int_key():
    with pytest.raises(ValueError):
        some_obj = KeyValueStorage("homework/homework8/task1_example_wrong.txt")
