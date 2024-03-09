#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    the_list = [[1] * s for s in range(1, n + 1)]
    for i in range(n):
        for j in range(i):
            if j not in [0, i]:
                the_list[i][j] = the_list[i - 1][j] + the_list[i - 1][j - 1]
    return the_list
