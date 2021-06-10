#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if min([a, b, c]) <= 0:
        raise TriangleError("Side lengths must be greater than zero")

    sorted_lengths = sorted([a, b, c])
    if sorted_lengths[0] + sorted_lengths[1] <= sorted_lengths[2]:
        raise TriangleError("No side can be longer than the sum of the other two sides")
    # My first solution:
    #if unique_side_lengths == 1:
    #    return 'equilateral'
    #elif unique_side_lengths == 2:
    #    return 'isosceles'
    #else:
    #    return 'scalene'

    # Second solution - may be more Pythonic?
    triangle_types = {
        1: 'equilateral',
        2: 'isosceles',
        3: 'scalene'
    }
    unique_side_lengths = len(set([a, b, c]))
    return triangle_types.get(unique_side_lengths, "Invalid triangle")

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
