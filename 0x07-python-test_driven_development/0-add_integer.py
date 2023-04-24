#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The example module supplies one function, add_integer(). For example,

>>> add_integer(5, 3)
8
"""
def add_integer(a, b=98):
    """
        Adds two integers.
        Args:
            a (int|float): An integer or floating point number
            b (int|float): An integer or floating point number
        Returns: The sum of `a` and `b`
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)