import sqlite3

import pytest

from homework.homework8.hw2 import TableData

presidents = TableData("homework/homework8/example.sqlite", "presidents")


def test_regular_case():
    assert presidents["Yeltsin"] == [("Yeltsin", 999, "Russia")]
    assert len(presidents) == 3
    assert "Trump" in presidents
    for president in presidents:
        assert president["name"] == "Yeltsin"
        assert president["age"] == 999
        break
    for president in presidents:
        assert president["name"] == "Trump"
        assert president["age"] == 1337
        break


def test_change_case():
    presidents.cursor.execute(
        "UPDATE presidents SET name = 'Putin' WHERE name = 'Yeltsin'"
    )
    assert presidents["Putin"] == [("Putin", 999, "Russia")]
