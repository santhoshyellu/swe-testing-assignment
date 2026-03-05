"""
Integration tests for the Calculator class.
Tests the interaction between input layer and calculation logic.
"""

import pytest
from src.calculator import Calculator


class TestCalculatorIntegration:
    """Integration tests for complete calculator workflows."""

    def test_full_addition_workflow(self):
        """
        Integration test: Simulate user input for "5 + 3 = 8".
        Tests: digit input -> operation -> digit input -> calculate
        """
        calc = Calculator()

        # User enters: 5
        calc.input_digit("5")
        assert calc.get_display() == "5"

        # User presses: +
        calc.set_operation("+")
        assert calc.pending_operation == "+"
        assert calc.pending_value == 5.0

        # User enters: 3
        calc.input_digit("3")
        assert calc.get_display() == "3"

        # User presses: =
        result = calc.calculate()
        assert result == 8
        assert calc.get_display() == "8"

    def test_clear_after_calculation(self):
        """
        Integration test: Verify pressing Clear after calculation resets display.
        Tests: multi-step calculation -> clear -> verify reset
        """
        calc = Calculator()

        # Perform a calculation: 10 - 4 = 6
        calc.input_digit("1")
        calc.input_digit("0")
        calc.set_operation("-")
        calc.input_digit("4")
        result = calc.calculate()
        assert result == 6

        # Press Clear
        calc.clear()
        assert calc.get_display() == "0"
        assert calc.current_value == 0
        assert calc.pending_operation is None

    def test_chained_operations(self):
        """
        Integration test: Perform chained operations "2 * 3 + 4 = 10".
        Tests: multiple operations in sequence
        """
        calc = Calculator()

        # User enters: 2
        calc.input_digit("2")

        # User presses: *
        calc.set_operation("*")

        # User enters: 3
        calc.input_digit("3")

        # User presses: + (should complete 2 * 3 = 6)
        calc.set_operation("+")
        assert float(calc.get_display()) == 6.0

        # User enters: 4
        calc.input_digit("4")

        # User presses: =
        result = calc.calculate()
        assert result == 10
        assert calc.get_display() == "10"

    def test_decimal_input_workflow(self):
        """
        Integration test: User enters decimal number "3.14".
        Tests: digit input + decimal point + more digits
        """
        calc = Calculator()

        # User enters: 3
        calc.input_digit("3")
        assert calc.get_display() == "3"

        # User enters: .
        calc.input_decimal()
        assert calc.get_display() == "3."

        # User enters: 1
        calc.input_digit("1")
        assert calc.get_display() == "3.1"

        # User enters: 4
        calc.input_digit("4")
        assert calc.get_display() == "3.14"

    def test_division_by_zero_handling(self):
        """
        Integration test: User attempts to divide by zero "10 / 0".
        Tests: error handling in integrated workflow
        """
        calc = Calculator()

        # User enters: 1, 0
        calc.input_digit("1")
        calc.input_digit("0")

        # User presses: /
        calc.set_operation("/")

        # User enters: 0
        calc.input_digit("0")

        # User presses: =, expecting error
        with pytest.raises(ValueError, match="Division by zero"):
            calc.calculate()
