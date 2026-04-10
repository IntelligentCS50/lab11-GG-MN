# https://github.com/IntelligentCS50/lab11-GG-MN
# Partner 1: Gideon Goldmann
# Partner 2: Chantelle Monae Nera

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

def mul(a, b):
    return multiply(a, b)

def div(a, b):
    return divide(a, b)

def exp(a, b):
    return exponent(a, b)
