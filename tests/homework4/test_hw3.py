import pytest

from homework.homework4.hw3 import my_precious_logger


def test_error_case(capsys):
    my_precious_logger("error: you win this game")
    captured = capsys.readouterr()
    assert captured.err == "error: you win this game"


def test_out_case(capsys):
    my_precious_logger("This is not error: you win this game")
    captured = capsys.readouterr()
    assert captured.out == "This is not error: you win this game"
