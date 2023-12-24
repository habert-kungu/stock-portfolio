import pytest
from advanced_culculator  import add, subtract, multiply, divide, exponent, sin, cos, tan, log

def test_add():
    assert add(5, 3) == 8

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(5, 3) == 15

def test_divide():
    assert divide(5, 3) == 1.6666666666666667

def test_exponent():
    assert exponent(5, 3) == 125

def test_sin():
    assert sin(0) == 0.0

def test_cos():
    assert cos(0) == 1.0

def test_tan():
    assert tan(0) == 0.0

def test_log():
    assert log(10, 10) == 1.0