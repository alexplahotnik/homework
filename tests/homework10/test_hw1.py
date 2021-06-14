import sys

import pytest

from homework.homework10.hw1 import *


def test_get_main_page_with_monkeypatch(monkeypatch):
    this_module = sys.modules[__name__]
    monkeypatch.setattr(this_module, "get_dollar_rate", lambda: 71.6797)
    with open("tests/homework10/s&p_500.txt") as f:
        html = f.read()
    assert get_main_page_info([html, "html"]) == [
        ["3M", "mmm-stock", 14540.227144999999, 22.16],
        ["AO Smith", "aos-stock", 4941.598518, 38.7],
        ["Abbott Laboratories", "abt-stock", 7874.731841999999, 19.46],
        ["AbbVie", "abbv-stock", 8271.83738, 16.86],
        ["Accenture", "acn-stock", 20500.3942, 35.73],
        ["Activision Blizzard", "atvi-stock", 7049.698495, 34.44],
        ["Adobe", "adbe-stock", 39137.1162, 28.21],
        ["Advance Auto Parts", "aap-stock", 14282.897022, 37.19],
        ["AES", "aes-stock", 1862.238606, 82.88],
        ["Aflac", "afl-stock", 4031.9831249999997, 42.43],
    ]


def test_adobe_personal_page():
    with open("tests/homework10/Adobe.txt", "r") as f:
        html = f.read()
    assert get_company_page_info(html) == [47.1, 41.969095369363444]
