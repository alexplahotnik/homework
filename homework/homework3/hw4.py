def is_armstrong(number: int) -> bool:
    """Function, that check armstrong numbers"""

    def raised_digit(digit: str) -> int:
        return int(digit) ** len(str(number))

    return sum(map(raised_digit, [digit for digit in str(number)])) == number
