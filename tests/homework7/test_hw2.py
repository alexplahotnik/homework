import pytest

from homework.homework7.hw2 import backspace_compare


def test_backspace_first_last_symbol():
    assert backspace_compare("##as#r", "ew##aqp##rf#")


def test_no_backspace():
    assert not backspace_compare("we", "wr")


def test_same_symbol():
    assert backspace_compare("ww#w#w", "wq#w")
