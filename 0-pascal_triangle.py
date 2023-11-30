#!/usr/bin/python3
""" A python module that returns a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    """A function thst returns a list of lists of integers representing the Pascal’s triangle of n"""


    triangle = []

    for col in range(n):
        new_row = []
        for row in range(col + 1):
            if row == 0 or col == row:
                new_row.append(1)
            else:
                new_row.append(triangle[col - 1][row] + triangle[col - 1][row - 1])
        triangle.append(new_row)
    return triangle

result = pascal_triangle(5)

for row in result:
    print (row)
