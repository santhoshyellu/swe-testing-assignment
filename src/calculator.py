"""
Quick-Calc: A simple calculator application.
Provides core calculation operations: addition, subtraction, multiplication, and division.
"""


class Calculator:
    """A simple calculator that performs basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator with display value at zero."""
        self.current_value = 0
        self.display = "0"
        self.pending_operation = None
        self.pending_value = None
        self.new_number = True

    def add(self, a, b):
        """
        Add two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Sum of a and b
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract b from a.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Difference of a and b
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Args:
            a (float): First number
            b (float): Second number

        Returns:
            float: Product of a and b
        """
        return a * b

    def divide(self, a, b):
        """
        Divide a by b.

        Args:
            a (float): Dividend
            b (float): Divisor

        Raises:
            ValueError: If b is zero

        Returns:
            float: Quotient of a and b
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def clear(self):
        """Reset the calculator to initial state."""
        self.current_value = 0
        self.display = "0"
        self.pending_operation = None
        self.pending_value = None
        self.new_number = True

    def input_digit(self, digit):
        """
        Input a digit (0-9).

        Args:
            digit (str): A single digit character ('0'-'9')
        """
        if not digit.isdigit():
            raise ValueError("Input must be a single digit")

        if self.new_number:
            self.display = digit
            self.new_number = False
        else:
            if self.display == "0":
                self.display = digit
            else:
                self.display += digit

        self.current_value = float(self.display)

    def input_decimal(self):
        """Add a decimal point to the current input."""
        if self.new_number:
            self.display = "0."
            self.new_number = False
        else:
            if "." not in self.display:
                self.display += "."

    def set_operation(self, operation):
        """
        Set a pending operation (+, -, *, /).

        Args:
            operation (str): Operation character ('+', '-', '*', '/')
        """
        if self.pending_operation is not None and not self.new_number:
            # Complete the previous operation
            self.calculate()

        self.pending_operation = operation
        self.pending_value = self.current_value
        self.new_number = True

    def calculate(self):
        """
        Execute the pending operation and return the result.

        Returns:
            float: The result of the calculation

        Raises:
            ValueError: If division by zero is attempted
        """
        if self.pending_operation is None:
            return self.current_value

        if self.pending_operation == "+":
            result = self.add(self.pending_value, self.current_value)
        elif self.pending_operation == "-":
            result = self.subtract(self.pending_value, self.current_value)
        elif self.pending_operation == "*":
            result = self.multiply(self.pending_value, self.current_value)
        elif self.pending_operation == "/":
            result = self.divide(self.pending_value, self.current_value)
        else:
            return self.current_value

        self.current_value = result
        # Display integers without decimal point
        if isinstance(result, float) and result.is_integer():
            self.display = str(int(result))
        else:
            self.display = str(result)
        self.pending_operation = None
        self.pending_value = None
        self.new_number = True

        return result

    def get_display(self):
        """
        Get the current display value.

        Returns:
            str: The display string
        """
        return self.display
