#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list which takes a list mxd_lst of
integers and floats and returns their sum as a float.
"""


def sum_mixed_list(input_list: float) -> float:
    """ Sum_mixed_list function """
    for i in range(len(input_list)):
        i += 1
    return sum(input_list)
