#!/usr/bin/python3
def print_last_digit(number):
    """Print and return last digit"""
    n = abs(number)
    while n > 9:
        n /= 10
    print(f"{n}", end="")
    return n
