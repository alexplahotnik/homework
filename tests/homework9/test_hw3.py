from pathlib import Path

import pytest

from homework.homework9.hw3 import *


def test_no_tokenizer():
    assert universal_file_counter("tests/homework9/examples/", "py") == 3


def test_with_tokenizer():
    def easy_tokenizer(data):
        yield from data.split()

    assert (
        universal_file_counter("tests/homework9/examples/", "py", easy_tokenizer) == 5
    )


def test_other_extensions():
    assert universal_file_counter("tests/homework9/examples/", "txt") == 11
