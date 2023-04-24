#!/usr/bin/python3
"""
This is the "3-say_my_name" module.

The example module supplies one function, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first name> <last name>
        Args:
            first_name (string): A string.
            last_name (string): A string.
    """
    name1_err = "first_name must be a string"
    name2_err = "last_name must be a string"
    if not first_name or type(first_name) is not str:
        raise TypeError(name1_err)
    if type(last_name) is not str:
        raise TypeError(name2_err)
    print("My name is {} {}".format(first_name, last_name))
