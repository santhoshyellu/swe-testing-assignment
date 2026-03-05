"""
Unit tests for the Calculator class.
Tests individual arithmetic operations and edge cases.
"""

import pytest
from src.calculator import Calculator


class TestAddition:
    """Test addition operation."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        calc = Calculator()
        result = calc.add(5, 3)
        assert result == 8

    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        calc = Calculator()
        result = calc.add(-5, -3)
        assert result == -8

    def test_add_mixed_signs(self):
        """Test addition with mixed positive and negative numbers."""
        calc = Calculator()
        result = calc.add(10, -4)
        assert result == 6


class TestSubtraction:
    """Test subtraction operation."""

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        calc = Calculator()
        result = calc.subtract(10, 4)
        assert result == 6

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        calc = Calculator()
        result = calc.subtract(-5, -3)
        assert result == -2

    def test_subtract_negative_result(self):
        """Test subtraction resulting in negative number."""
        calc = Calculator()
        result = calc.subtract(3, 5)
        assert result == -2


class TestMultiplication:
    """Test multiplication operation."""

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        calc = Calculator()
        result = calc.multiply(6, 7)
        assert result == 42

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        calc = Calculator()
        result = calc.multiply(100, 0)
        assert result == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication with negative numbers."""
        calc = Calculator()
        result = calc.multiply(-3, -4)
        assert result == 12


class TestDivision:
    """Test division operation."""

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        calc = Calculator()
        result = calc.divide(10, 2)
        assert result == 5

    def test_divide_decimal_result(self):
        """Test division resulting in decimal."""
        calc = Calculator()
        result = calc.divide(5, 2)
        assert result == 2.5

    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        calc = Calculator()
        with pytest.raises(ValueError, match="Division by zero"):
            calc.divide(10, 0)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        calc = Calculator()
        result = calc.divide(-10, 2)
        assert result == -5


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_add_very_large_numbers(self):
        """Test addition of very large numbers."""
        calc = Calculator()
        result = calc.add(1e10, 2e10)
        assert result == 3e10

    def test_divide_very_small_numbers(self):
        """Test division resulting in very small numbers."""
        calc = Calculator()
        result = calc.divide(0.0001, 100)
        assert result == pytest.approx(0.000001)

    def test_multiply_decimals(self):
        """Test multiplication of decimal numbers."""
        calc = Calculator()
        result = calc.multiply(2.5, 4.0)
        assert result == 10.0

    def test_subtract_large_numbers(self):
        """Test subtraction of large numbers."""
        calc = Calculator()
        result = calc.subtract(1000000, 999999)
        assert result == 1


class TestClear:
    """Test clear functionality."""

    def test_clear_resets_to_zero(self):
        """Test that clear resets display to 0."""
        calc = Calculator()
        calc.input_digit("5")
        calc.clear()
        assert calc.get_display() == "0"
        assert calc.current_value == 0

    def test_clear_resets_pending_operation(self):
        """Test that clear resets pending operations."""
        calc = Calculator()
        calc.input_digit("5")
        calc.set_operation("+")
        calc.clear()
        assert calc.pending_operation is None
        assert calc.pending_value is None
