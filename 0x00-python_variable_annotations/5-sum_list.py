#!/usr/bin/env python3
"""
Module for type-annotated function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums the elements
    """
    return sum(input_list)
