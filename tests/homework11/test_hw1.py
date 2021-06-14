import pytest

from homework.homework11.hw1 import *


def test_meta_parameters():
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
