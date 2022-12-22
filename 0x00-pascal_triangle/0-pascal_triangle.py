#!/usr/bin/python3
""" pascal triangle 
"""

from math import factorial


def pascal_triangle(n):
    """ returns pascal triangle
    """
    if n <= 0:
        return []
    else:
        for i in range(n):
            for j in range(0, i + 1):
                print(end=" ")
            for j in range(i + 1):
