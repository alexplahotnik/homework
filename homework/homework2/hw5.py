"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(values, first_value, second_value=None, step=1):
    result = []
    values = list(values)
    if not second_value:
        if first_value not in values:
            return "Wrong values"
        for value in values[: values.index(first_value) : step]:
            result.append(value)
    else:
        if first_value not in values or second_value not in values:
            return "Wrong values"
        for value in values[
            values.index(first_value) : values.index(second_value) : step
        ]:
            result.append(value)
    return result
