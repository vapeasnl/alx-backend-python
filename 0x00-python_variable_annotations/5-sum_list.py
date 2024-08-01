#!/usr/bin/env python3
"""
Module for type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float.
"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Sums the elements of the input list and returns the result as a float.
    """
    return sum(input_list)
