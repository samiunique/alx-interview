#!/usr/bin/python3
"""
This module provides a function to generate Pascal's triangle.
"""

from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generate Pascal's triangle of size `n`.

    Args:
        n (int): The number of levels in the Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists, where each sublist represents a level in the Pascal's triangle.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    if n == 2:
        return [[1], [1, 1]]

    triangle = [[1], [1, 1]]

    for i in range(2, n):
        temp = [1, 1]
        for j in range(len(triangle[-1]) - 1):
            a = triangle[-1][j]
            b = triangle[-1][j + 1]
            temp.insert(-1, a + b)
        triangle.append(temp)

    return triangle