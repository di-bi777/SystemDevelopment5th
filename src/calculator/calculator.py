"""
A simple calculator module with basic arithmetic operations.
"""


class InvalidInputException(Exception):
    """Exception raised when input values are outside the valid range."""

    pass


class Calculator:
    """Calculator class providing basic arithmetic operations."""

    def _validate(self, a, b):
        MIN_VALUE = -1_000_000
        MAX_VALUE = 1_000_000

        if not (MIN_VALUE <= a <= MAX_VALUE):
            raise InvalidInputException(f"Invalid input: {a}")

        if not (MIN_VALUE <= b <= MAX_VALUE):
            raise InvalidInputException(f"Invalid input: {b}")

    def add(self, a, b):
        """Add two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Sum of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate(a, b)
        return a + b

    def subtract(self, a, b):
        """Subtract b from a.

        Args:
            a: First number
            b: Second number

        Returns:
            Difference of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate(a, b)
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            Product of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
        """
        self._validate(a, b)
        return a * b

    def divide(self, a, b):
        """Divide a by b.

        Args:
            a: Numerator
            b: Denominator

        Returns:
            Quotient of a and b

        Raises:
            InvalidInputException: If any input is outside valid range
            ValueError: If b is zero
        """
        self._validate(a, b)
        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b
