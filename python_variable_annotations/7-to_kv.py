#!/usr/bin/env python3
"""Defines the 'to_kv' function."""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Returns a tuple with the string and the square of the number.

    Parameters:
        k (str): A string.
        v (int/float): An int or float value.

    Returns: (str, float) Whatever that is."""

    return (k, v ** 2)
