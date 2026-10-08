"""Task 5: Simple Calculator.

Command-line calculator providing basic arithmetic operations (+, -, *, /)
with robust error handling for division by zero, invalid operators, and non-numeric inputs.
"""

from typing import Union

Number = Union[int, float]


def calculate(first_number: Number, operator: str, second_number: Number) -> Number:
    """Perform basic arithmetic calculations.

    Args:
        first_number: First numeric value.
        operator: Arithmetic operator ('+', '-', '*', '/').
        second_number: Second numeric value.

    Returns:
        Result of calculation (int or float).

    Raises:
        ZeroDivisionError: If second_number is 0 during division.
        ValueError: If operator is unsupported.
        TypeError: If inputs are non-numeric.
    """
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError("Inputs must be numbers.")

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = first_number / second_number
    else:
        raise ValueError(f"Invalid operator '{operator}'. Supported operators: +, -, *, /")

    # Format result to int if it represents an exact integer
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


def run_interactive_calculator() -> None:
    """Run interactive CLI calculator session."""
    print("\n--- Interactive Calculator ---")
    try:
        raw_first = input("Enter first number: ").strip()
        first_num = float(raw_first)

        operator = input("Enter operator (+, -, *, /): ").strip()

        raw_second = input("Enter second number: ").strip()
        second_num = float(raw_second)
    except (KeyboardInterrupt, EOFError):
        print("Interactive session ended.")
        return
    except ValueError:
        print("Error: Invalid numeric input.")
        return

    try:
        result = calculate(first_num, operator, second_num)
        fmt_first = int(first_num) if first_num.is_integer() else first_num
        fmt_second = int(second_num) if second_num.is_integer() else second_num
        print(f"Output: {fmt_first} {operator} {fmt_second} = {result}")
    except (ZeroDivisionError, ValueError, TypeError) as err:
        print(f"Output:\nError: {err}")


def run_demo() -> None:
    """Run demonstration test cases for Task 5."""
    print("=" * 40)
    print("TASK 5: SIMPLE CALCULATOR DEMO")
    print("=" * 40)

    test_cases = [
        (20, "+", 10, "Addition"),
        (20, "-", 10, "Subtraction"),
        (20, "*", 10, "Multiplication"),
        (20, "/", 10, "Division"),
        (20, "/", 0, "Division by zero"),
        (20, "%", 10, "Invalid operator"),
    ]

    for num1, op, num2, desc in test_cases:
        try:
            res = calculate(num1, op, num2)
            print(f"[{desc}] {num1} {op} {num2} = {res}")
        except (ZeroDivisionError, ValueError, TypeError) as e:
            print(f"[{desc}] {num1} {op} {num2} -> Error: {e}")

    print("=" * 40)


if __name__ == "__main__":
    run_demo()
    run_interactive_calculator()
