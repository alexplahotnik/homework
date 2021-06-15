from unittest.mock import MagicMock

import pytest

from homework.homework4.hw2 import Count


def test_with_file():
    html = Count()
    html._get_html = MagicMock(
        return_value='<meta name="viewport" content="width=device-width, initial-scale=1" />'
    )
    numbers_i = html.count_dots_on_i("https://example.com/")
    assert numbers_i == 7


def test_without_file():
    test_obj = Count()
    with pytest.raises(ValueError):
        test_obj.count_dots_on_i("https://example123123.com/")
