import pytest

from homework.homework9.hw2 import *


def test_class_supressor():
    with SuppressorClass():
        assert not [][2]


def test_func_supressor():
    with suppressor_function():
        assert not [][2]
