#!/usr/bin/env python3
"""
Write a type-annotated function to_str that takes a float n as argument and
returns the string representation of the float.
"""

import math


def to_str(n: float) -> str:
    """ Floor function """
    return math.floor(n)
