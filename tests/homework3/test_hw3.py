import pytest

from homework.homework3.hw3 import *


def test_with_good_arguments():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]


def test_key_from_different_source():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert make_filter(name="polly", type="person").apply(sample_data) == []


def test_wrong_key():
    sample_data = [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        },
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    ]
    assert make_filter(name="polly", city="Paris").apply(sample_data) == []
