import pytest

from homework.homework4.hw5 import fizzbuzz


def test_empty_list():
    assert list(fizzbuzz(0)) == []


def test_five_elements():
    assert list(fizzbuzz(5)) == ["1", "2", "fizz", "4", "buzz"]


def test_fizzbuzz_case():
    assert list(fizzbuzz(16)) == [
        "1",
        "2",
        "fizz",
        "4",
        "buzz",
        "fizz",
        "7",
        "8",
        "fizz",
        "buzz",
        "11",
        "fizz",
        "13",
        "14",
        "fizzbuzz",
        "16",
    ]
