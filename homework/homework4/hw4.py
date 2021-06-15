from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    How to run doctest:
    - Install Python 3.8 (https://www.python.org/downloads/)
    - Open terminal
    - Run script using command "python <path_to_script>/<script_name>"
    - If all tests will be pass, it will be nothing to return
    - For detailed information use "-v" command after script name

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']

    >>> fizzbuzz(0)
    []

    >>> fizzbuzz(15)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("fizzbuzz")
        elif i % 3 == 0:
            result.append("fizz")
        elif i % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
