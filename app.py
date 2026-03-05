#!/usr/bin/env python3
"""
Interactive CLI for Quick-Calc Calculator
"""

from src.calculator import Calculator


def print_menu():
    """Display the calculator menu."""
    print("\n" + "=" * 50)
    print("Quick-Calc - Interactive Calculator")
    print("=" * 50)
    print("Commands:")
    print("  <digit>  - Input a digit (0-9)")
    print("  .        - Add decimal point")
    print("  +, -, *, / - Set operation")
    print("  =        - Calculate result")
    print("  c        - Clear calculator")
    print("  q        - Quit")
    print("=" * 50)


def main():
    """Run the interactive calculator."""
    calc = Calculator()
    print_menu()

    while True:
        print(f"\nDisplay: {calc.get_display()}")
        user_input = input("Enter command: ").strip().lower()

        if not user_input:
            continue

        try:
            if user_input == "q":
                print("Goodbye!")
                break

            elif user_input == "c":
                calc.clear()
                print("Calculator cleared")

            elif user_input == "=":
                result = calc.calculate()
                print(f"Result: {calc.get_display()}")

            elif user_input in "+-*/":
                calc.set_operation(user_input)
                print(f"Operation set: {user_input}")

            elif user_input == ".":
                calc.input_decimal()
                print(f"Decimal added: {calc.get_display()}")

            elif user_input.isdigit() and len(user_input) == 1:
                calc.input_digit(user_input)
                print(f"Digit entered: {calc.get_display()}")

            else:
                print("Invalid input. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
