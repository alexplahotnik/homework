from typing import Generator


def fizzbuzz(n: int) -> Generator:
    numbers = [str(i) for i in range(1, n + 1)]
    for index in range(2, n, 3):
        numbers[index] = "fizz"
    for index in range(4, n, 5):
        numbers[index] = "buzz"
    for index in range(14, n, 15):
        numbers[index] = "fizzbuzz"
    for number in numbers:
        yield number


print(list(fizzbuzz(16)))
