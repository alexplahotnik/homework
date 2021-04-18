import pytest

from homework.homework2.hw1 import *


def test_longest_unique():
    """Testing first function"""
    assert get_longest_diverse_words("tests/homework2/test_text.txt") == [
        "hinausführen",
        "vorgebahnte",
        "Betrachtung",
        "bedenklichen",
        "verbirgt",
        "vielmehr",
        "Waldgang",
        "Ausflug",
        "sondern",
        "hinter",
    ]


def test_rarest_char():
    """Testing second function"""
    assert set(get_rarest_char("tests/homework2/test_text.txt")) == {
        "w",
        "S",
        "B",
        "Ü",
        "y",
        "»",
        "«",
        "—",
        "I",
        "1",
        "P",
    }


def test_count_punctuation():
    """Testing third function"""
    assert count_punctuation_chars("tests/homework2/test_text.txt") == 10


def test_count_nonascii():
    """Testing fourth function"""
    assert count_non_ascii_chars("tests/homework2/test_text.txt") == 9


def test_common_nonascii():
    """Testimg last function"""
    assert set(get_most_common_non_ascii_char("tests/homework2/test_text.txt")) == {"ü"}
