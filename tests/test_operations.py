import pytest
from calculator.operations import addition, divide, multiply, subtraction


def test_addition():
    assert addition(3, 7) == 10


def test_subtraction():
    assert subtraction(10, 3) == 7


def test_multiply():
    assert multiply(6, 7) == 42
    assert multiply(-2, 5) == -10


def test_divide():
    assert divide(8, 2) == 4
    assert divide(-9, 3) == -3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
