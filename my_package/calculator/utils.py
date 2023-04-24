def validate_numbers(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        raise TypeError("Both arguments must be numbers.")


def display_result(operation, result):
    print(f"The result of the {operation} operation is: {result}")