from typing import Union


Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    return x + y


def subtract(x: Number, y: Number) -> Number:
    return x - y


def multiply(x: Number, y: Number) -> Number:
    return x * y


def divide(x: Number, y: Number) -> Number:
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y
