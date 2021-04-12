from typing import Sequence


def _check_window(x: int, y: int, z: int) -> bool:
    """Checking the basic condition for three numbers"""
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    """The function checks that it is a fibonacci sequence"""
    if len(data) < 3:
        raise ValueError("Not enough data entered")
    while len(data) >= 3:
        a, b, c = data[0], data[1], data[2]
        if not _check_window(a, b, c):
            return False
        del data[0]
    return True
