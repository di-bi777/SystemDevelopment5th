"""
Test suite for the Calculator class.
"""

import pytest
import sys
from calculator.calculator import Calculator, InvalidInputException

def calc():
    return Calculator()


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        calc = Calculator()
        a = 5
        b = 3
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        calc = Calculator()
        a = 5
        b = 3
        expected = 15

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        calc = Calculator()
        a = 15
        b = 3
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected
    def test_divide_by_zero_should_raise_error(self):
        """0で割ろうとしたらValueErrorになるべき"""
        calc = Calculator()
        with pytest.raises(ValueError) as exc_info:
            calc.divide(10, 0)
        assert str(exc_info.value) == "Cannot divide by zero"


class TestInputValidation:

    def test_too_large_value_should_raise_exception(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1_000_001, 10)

    def test_too_small_value_should_raise_exception(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(-1_000_001, 10)

    def test_boundary_min_value_should_be_valid(self):
        """最小値ちょうど(-1,000,000)は有効な入力であるべき"""
        calc = Calculator()
        
        assert calc.add(-1_000_000, 0) == -1_000_000

    def test_boundary_max_value_should_be_valid(self):
        """最大値ちょうど(1,000,000)は有効な入力であるべき"""
        calc = Calculator()
        
        assert calc.add(1_000_000, 0) == 1_000_000
    
    def test_too_large_value_should_raise_exception_with_message(self):
        calc = Calculator()
        
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(1_000_001, 10)
        
        
        assert "Invalid input" in str(exc_info.value)

    def test_too_small_value_should_raise_exception_with_message(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(-1_000_001, 10)
            
        assert "Invalid input" in str(exc_info.value)

    def test_boundary_min_value_for_b_should_be_valid(self):
        """2つ目の引数が最小値ちょうど(-1,000,000)でも有効であるべき"""
        calc = Calculator()
        
        assert calc.add(0, -1_000_000) == -1_000_000

    def test_boundary_max_value_for_b_should_be_valid(self):
        """2つ目の引数が最大値ちょうど(1,000,000)でも有効であるべき"""
        calc = Calculator()
        
        assert calc.add(0, 1_000_000) == 1_000_000

    def test_invalid_b_value_should_raise_exception_with_message(self):
        """2つ目の引数が無効な場合、適切なメッセージが出るべき"""
        calc = Calculator()
        
        with pytest.raises(InvalidInputException) as exc_info:
            calc.add(0, 1_000_001)
        
        assert "Invalid input" in str(exc_info.value)
    
