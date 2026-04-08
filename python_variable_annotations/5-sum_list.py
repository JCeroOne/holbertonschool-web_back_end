#!/usr/bin/env python3
"""Defines the 'sum_list' function."""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Adds all the values of a list of floats together.

    Parameters:
        input_list (list[float]): The list of numbers.

    Returns: (float) The sum of all the values."""

    return sum(input_list)
