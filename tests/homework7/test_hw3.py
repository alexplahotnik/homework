import pytest

from homework.homework7.hw3 import tic_tac_toe_checker


def test_x_wins():
    assert (
        tic_tac_toe_checker([["o", "x", "o"], ["o", "-", "o"], ["x", "x", "x"]])
        == "x wins!"
    )


def test_o_wins():
    assert (
        tic_tac_toe_checker([["x", "x", "o"], ["-", "o", "-"], ["o", "x", "o"]])
        == "o wins!"
    )


def test_draw():
    assert (
        tic_tac_toe_checker([["o", "x", "o"], ["x", "o", "o"], ["x", "o", "x"]])
        == "draw!"
    )


def test_unfinished():
    assert (
        tic_tac_toe_checker([["o", "x", "o"], ["x", "-", "o"], ["x", "o", "x"]])
        == "unfinished"
    )
