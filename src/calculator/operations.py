"""Basic calculator operations with safe divide."""

def addition(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b

def subtraction(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b

def divide(a: float, b: float) -> float:
    """Return a divided by b. Raises ZeroDivisionError on b == 0."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
