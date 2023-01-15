#!/usr/bin/python3
""" Minimum Operations module
"""


def minOperations(n: int) -> int:
    """ Returns the minimum number of operations
    """
    a = 0
    b = 2
    while n > 1:
        while n % b == 0:
            a += b
            n = n / b
        b += 1
    return a
