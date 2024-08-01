#!/usr/bin/env python3
"""
Module for type-annotated function to_kv that takes a string k and an int OR float v as arguments and returns a tuple.
"""
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string k as the first element and the square of v as the second element (annotated as float).
    """
    return (k, v * v)
