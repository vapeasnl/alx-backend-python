#!/usr/bin/env python3
"""
Module for type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that takes a float
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
