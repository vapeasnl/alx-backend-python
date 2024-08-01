#!/usr/bin/env python3
"""
Module for type-annotated function sum_mixed_list
"""
from typing import List, Union

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums the elements
    """
    return sum(mxd_lst)
