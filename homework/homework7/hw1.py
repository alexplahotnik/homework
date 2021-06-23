from typing import Any


def find_occurrences(tree: dict, element: Any) -> int:
    """Find and count all occurrences of element in the tree"""
    counter = 0
    for key, values in tree.items():
        if key == element:
            counter += 1
        if isinstance(values, dict):
            counter += find_occurrences(values, element)
        elif type(values) in (tuple, set, list):
            new_tree = {key: value for key, value in zip(range(len(values)), values)}
            counter += find_occurrences(new_tree, element)
        elif values == element:
            counter += 1
    return counter
