from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Finding max and min values in file"""
    with open(file_name) as f:
        lines = f.readlines()
    maximum, minimum = int(lines[0]), int(lines[0])
    for line in lines:
        if int(line) > maximum:
            maximum = int(line)
        elif int(line) < minimum:
            minimum = int(line)
    return (minimum, maximum)
