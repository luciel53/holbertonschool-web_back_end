#!/usr/bin/env python3
"""
Write a type-annotated function sum_list which takes a list input_list of
floats as argument and returns their sum as a float.
"""


def sum_list(input_list: float) -> float:
    """ Sum_list function """
    for i in range(len(input_list)):
        i += 1
    return sum(input_list)
