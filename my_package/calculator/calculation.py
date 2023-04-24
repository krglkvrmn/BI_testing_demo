from typing import Literal

from my_package.calculator.operations import add, subtract, multiply, divide, Number
from my_package.calculator.utils import validate_numbers


def calculate(x: Number, y: Number, operation: Literal["+", "-", "*", "/"]) -> Number:
    validate_numbers(x, y)

    if operation == "+":
        result = add(x, y)
    elif operation == "-":
        result = subtract(x, y)
    elif operation == "*":
        result = multiply(x, y)
    elif operation == "/":
        result = divide(x, y)
    else:
        raise ValueError("Invalid operation.")
    
    return result
