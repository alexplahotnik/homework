import pytest

from homework.homework3.hw4 import is_armstrong


def test_is_armstrong():
    assert is_armstrong(153) is True


def test_is_no_armstrong():
    assert is_armstrong(10) is False
