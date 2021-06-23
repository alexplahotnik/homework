import pytest

from homework.homework11.hw2 import *


def test_strategy_pattern():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 50

    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
