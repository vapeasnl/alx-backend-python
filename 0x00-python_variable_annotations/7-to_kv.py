#!/usr/bin/env python3
"""
Module for type-annotated function to_kv
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple
    """
    return (k, v * v)
