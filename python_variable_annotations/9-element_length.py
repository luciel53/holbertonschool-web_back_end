#!/usr/bin/env python3
"""
Annotate the below function’s parameters and return values with the
appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

"""

from typing import Union, List, Tuple, Callable, Sequence, Iterable
import math


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ element_length function annotated """
    return [(i, len(i)) for i in lst]
