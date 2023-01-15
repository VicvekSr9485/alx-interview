#!/usr/bin/python3
""" Minimum Operations module
"""


def minOperations(n: int) -> int:
    """ Returns the minimum number of operations
    """
    counter = 0

    if n <= 1:
        return counter

    for i in range(2, n + 1):
        while (0 == n % i):
            counter = counter + i
            n = n / i
            if n < i:
                break
    return counter
