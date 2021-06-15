import time

import pytest

from homework.homework3.hw2 import *


def test_time_slow_calc():
    start_time = time.time()
    data = range(500)
    result = work_slow_calculate(data)
    end_time = time.time()
    assert result == 1024259
    assert end_time - start_time < 60
