#!/usr/bin/env python3
"""Defines the function 'make_multiplier'."""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Returns a function that multiplies a number by a specific value.

    Parameters:
        multiplier (float): The number to multiply by.

    Returns: (function(float): float) What the description says."""

    return lambda x: x * multiplier
